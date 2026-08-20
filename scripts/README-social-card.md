# Social-card provenance

`images/social-card.jpg` uses the alpha-carbon backbone from a representative
thrombin model prepared by the Salsbury group for its published JCIM
hydrogen-bond project. The compact tube rendering is generated locally by
`scripts/render_social_card.py`; no model identifier or citation is printed on
the card itself.

The source file is `protein_Na_right_angle.pdb` in the group's archived project
files. The source coordinates are not copied into this public website
repository. To regenerate the card:

```sh
python3 scripts/render_social_card.py \
  --source /path/to/protein_Na_right_angle.pdb
```
