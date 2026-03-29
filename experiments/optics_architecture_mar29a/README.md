# 5 m optics architecture trade study

Run tag: `mar29a`

## Motivation
This sprint asks a narrow question: for a 5 m student-built radio telescope targeting H I, OH, and 22.235 GHz H2O, should Rev A use a prime-focus paraboloid or a secondary-fed architecture, and if a secondary is used, how large should it be?

The scientific bands are not required simultaneously. That relaxes the optical system substantially and means the burden of proof is on the secondary.

## Methods
This is a compact design-screening study, not a full physical-optics optimization. The comparison uses a weighted rubric intended to make the first build decision legible.

Architectures considered:
1. Prime-focus paraboloid with swappable feeds
2. On-axis classical Cassegrain
3. Oversized-secondary variant of an on-axis Cassegrain, included as a non-conventional option because oversizing can flatten central illumination at the main reflector and improve high-frequency aperture efficiency, at the expense of more blockage and stronger low-frequency penalties

Screening criteria:
- 22 GHz practicality, including receiver packaging and sensitivity to feed-support geometry
- low-band penalty from blockage and diffraction
- alignment burden
- fabrication complexity for an undergraduate team
- upgrade path

The score in `data/secondary_tradeoff.csv` is a normalized heuristic score from 0 to 1. It is not an electromagnetic simulation. The point of the plot is to expose trade direction and preferred size regime, not to claim percent-level performance.

Useful scale checks:
- 5 m dish half-power beamwidth is about 2.95 deg at H I, about 2.52 deg near the center of the OH band, and about 0.189 deg or 11.3 arcmin at 22.235 GHz
- simple geometric blockage from a circular secondary is `(d_secondary / 5 m)^2`
- at 22.235 GHz, surface quality better than about 0.5 mm rms is strongly desirable if the telescope is expected to be meaningfully efficient

## Results
The main plot is `plots/secondary_tradeoff.svg`.

How to read it:
- The horizontal line is the prime-focus baseline
- The two curves show how an on-axis Cassegrain trade changes as the secondary grows
- The classical curve peaks near 0.65 m
- The oversized-secondary curve shifts the best region upward in diameter, peaking around 0.8 m, but still stays below the prime-focus baseline in the total build score

Interpretation:
- For Rev A, prime focus is the best starting architecture
- It avoids an extra precision reflector, avoids strut and subreflector blockage at the H I and OH bands, and keeps the first system aligned around a single optical surface
- Because simultaneous multiband observing is not required, prime focus with swappable feeds captures most of the science with the least project risk

If a secondary is mandatory because the team wants the 22 GHz receiver off the feed legs or wants a more protected receiver location:
- preferred conventional size band: about 0.55 m to 0.75 m
- nominal recommendation inside that band: about 0.65 m
- non-conventional oversized option worth considering only if 22 GHz receiver packaging dominates the design: about 0.8 m
- larger values than about 0.9 m look hard to justify on a 5 m student-built dish because the low-band penalties and alignment burden rise faster than the packaging benefit

## Limitations
This sprint does not include:
- full physical-optics modeling of spillover, sidelobes, or diffraction from feed legs
- an optimized Gregorian design
- a structural finite-element analysis
- a real feed design at each band
- a tolerance stack for pointing, thermal drift, or gravity sag

Because of that, the score should be read as a first build decision aid, not as a final acceptance test.

## Next steps
1. Freeze Rev A as prime focus unless a hard receiver-placement requirement rules it out
2. If prime focus is accepted, split the work into:
   - low-band feed concept for 1.4 to 1.7 GHz
   - 22 GHz feed and receiver packaging
   - surface and pointing tolerance budget
3. If a secondary remains necessary, do a tighter second sprint around a 0.55 to 0.80 m classical Cassegrain with explicit feed-leg diffraction and illumination calculations
