#!/usr/bin/env python3
"""Create the site's social card from a group-authored molecular model."""

from __future__ import annotations

import argparse
import random
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw, ImageFont


WIDTH = 1200
HEIGHT = 630
SCALE = 2


def load_backbone(path: str) -> np.ndarray:
    """Read chain-A alpha carbons without exposing or copying the source PDB."""
    coordinates: list[tuple[float, float, float]] = []
    with Path(path).open(encoding="utf-8") as handle:
        for line in handle:
            if not line.startswith(("ATOM  ", "HETATM")):
                continue
            if line[12:16].strip() != "CA" or line[21:22] != "A":
                continue
            if line[16:17] not in {" ", "A"}:
                continue
            coordinates.append(
                (float(line[30:38]), float(line[38:46]), float(line[46:54]))
            )
    if len(coordinates) < 20:
        raise ValueError("The source does not contain a usable chain-A backbone")
    return np.asarray(coordinates, dtype=float)


def font(path: str, size: int) -> ImageFont.FreeTypeFont:
    return ImageFont.truetype(path, size * SCALE)


def draw_background(canvas: Image.Image) -> None:
    pixels = canvas.load()
    left = np.array([250.0, 247.0, 240.0])
    right = np.array([244.0, 238.0, 231.0])
    for x in range(canvas.width):
        mix = x / max(canvas.width - 1, 1)
        color = tuple(np.round(left * (1 - mix) + right * mix).astype(int))
        for y in range(canvas.height):
            pixels[x, y] = color


def draw_network(draw: ImageDraw.ImageDraw) -> None:
    random.seed(1)
    points = []
    for _ in range(24):
        x = random.randint(675, 1190) * SCALE
        y = random.randint(65, 605) * SCALE
        points.append((x, y))

    for i, point in enumerate(points):
        distances = sorted(
            ((point[0] - q[0]) ** 2 + (point[1] - q[1]) ** 2, q)
            for j, q in enumerate(points)
            if j != i
        )
        for _, neighbor in distances[:2]:
            draw.line([point, neighbor], fill=(116, 92, 77, 22), width=SCALE)

    for i, (x, y) in enumerate(points):
        radius = (2 if i % 4 else 3) * SCALE
        color = (155, 28, 49, 72) if i % 3 == 0 else (47, 58, 58, 46)
        draw.ellipse((x - radius, y - radius, x + radius, y + radius), fill=color)


def smooth_trace(points: np.ndarray, samples: int = 7) -> np.ndarray:
    """Catmull-Rom interpolation through a continuous backbone fragment."""
    if len(points) < 3:
        return points
    padded = np.vstack([points[0], points, points[-1]])
    output = []
    for i in range(1, len(padded) - 2):
        p0, p1, p2, p3 = padded[i - 1 : i + 3]
        for value in np.linspace(0.0, 1.0, samples, endpoint=False):
            value2 = value * value
            value3 = value2 * value
            output.append(
                0.5
                * (
                    (2.0 * p1)
                    + (-p0 + p2) * value
                    + (2.0 * p0 - 5.0 * p1 + 4.0 * p2 - p3) * value2
                    + (-p0 + 3.0 * p1 - 3.0 * p2 + p3) * value3
                )
            )
    output.append(points[-1])
    return np.asarray(output)


def project_backbone(coordinates: np.ndarray) -> tuple[list[np.ndarray], np.ndarray]:
    """Create a compact principal-axis view while retaining depth for shading."""
    centered = coordinates - coordinates.mean(axis=0)
    _, _, axes = np.linalg.svd(centered, full_matrices=False)
    rotated = centered @ axes.T

    # Keep successive residues together, but do not bridge genuine coordinate gaps.
    breaks = np.where(np.linalg.norm(np.diff(coordinates, axis=0), axis=1) > 6.0)[0] + 1
    fragments = np.split(rotated, breaks)
    fragments = [smooth_trace(fragment) for fragment in fragments if len(fragment) >= 2]
    all_points = np.vstack(fragments)
    return fragments, all_points


def draw_structure(
    overlay: Image.Image,
    coordinates: np.ndarray,
    box: tuple[int, int, int, int],
) -> None:
    fragments, all_points = project_backbone(coordinates)
    left, top, right, bottom = box
    projected = all_points[:, :2]
    low = projected.min(axis=0)
    high = projected.max(axis=0)
    span = np.maximum(high - low, 1.0)
    scale = min((right - left) / span[0], (bottom - top) / span[1])
    center = (low + high) / 2.0
    destination = np.array([(left + right) / 2.0, (top + bottom) / 2.0])

    fragment_paths = []
    segments = []
    for fragment in fragments:
        path = []
        for point in fragment:
            projected_point = (point[:2] - center) * scale + destination
            path.append((round(projected_point[0]), round(projected_point[1])))
        fragment_paths.append(path)
        for first, second in zip(fragment[:-1], fragment[1:]):
            p1 = (first[:2] - center) * scale + destination
            p2 = (second[:2] - center) * scale + destination
            segments.append(((tuple(p1), tuple(p2)), float((first[2] + second[2]) / 2.0)))

    depths = np.asarray([depth for _, depth in segments])
    depth_low, depth_high = float(depths.min()), float(depths.max())
    depth_span = max(depth_high - depth_low, 1.0)
    graphite = np.array([45.0, 58.0, 57.0])
    crimson = np.array([176.0, 24.0, 58.0])
    draw = ImageDraw.Draw(overlay, "RGBA")

    # Continuous under-strokes give the trace the visual mass of a molecular tube.
    for path in fragment_paths:
        shadow = [(x + 3 * SCALE, y + 4 * SCALE) for x, y in path]
        draw.line(shadow, fill=(29, 36, 36, 45), width=17 * SCALE, joint="curve")
        draw.line(path, fill=(24, 31, 31, 120), width=14 * SCALE, joint="curve")

    for (p1, p2), depth in sorted(segments, key=lambda item: item[1]):
        mix = (depth - depth_low) / depth_span
        color = np.round(graphite * (1.0 - mix) + crimson * mix).astype(int)
        width = 10 * SCALE
        points = [
            (round(p1[0]), round(p1[1])),
            (round(p2[0]), round(p2[1])),
        ]
        draw.line(points, fill=(*color, 252), width=width)


def build_card(coordinates: np.ndarray) -> Image.Image:
    canvas = Image.new("RGB", (WIDTH * SCALE, HEIGHT * SCALE))
    draw_background(canvas)

    overlay = Image.new("RGBA", canvas.size, (0, 0, 0, 0))
    overlay_draw = ImageDraw.Draw(overlay, "RGBA")
    draw_network(overlay_draw)
    draw_structure(
        overlay,
        coordinates,
        (735 * SCALE, 105 * SCALE, 1135 * SCALE, 525 * SCALE),
    )
    canvas = Image.alpha_composite(canvas.convert("RGBA"), overlay)

    draw = ImageDraw.Draw(canvas, "RGBA")
    crimson = (155, 28, 49, 255)
    ink = (25, 37, 39, 255)
    gold_dark = (117, 82, 23, 255)

    draw.rounded_rectangle(
        (49 * SCALE, 168 * SCALE, 205 * SCALE, 172 * SCALE),
        radius=2 * SCALE,
        fill=crimson,
    )

    title_font = font("/System/Library/Fonts/NewYork.ttf", 61)
    sans_font = font("/System/Library/Fonts/Avenir.ttc", 19)

    title_lines = ["Computational", "Molecular", "Biophysics Group"]
    y = 202 * SCALE
    line_height = 75 * SCALE
    for line in title_lines:
        draw.text((49 * SCALE, y), line, font=title_font, fill=ink, anchor="la")
        y += line_height

    draw.text(
        (52 * SCALE, 454 * SCALE),
        "Wake Forest University · Department of Physics",
        font=sans_font,
        fill=gold_dark,
        anchor="la",
    )

    return canvas.convert("RGB").resize((WIDTH, HEIGHT), Image.Resampling.LANCZOS)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", required=True, help="Local PDB model used for the card")
    parser.add_argument("--output", default="images/social-card.jpg")
    args = parser.parse_args()

    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    card = build_card(load_backbone(args.source))
    card.save(output, "JPEG", quality=94, optimize=True, progressive=True)


if __name__ == "__main__":
    main()
