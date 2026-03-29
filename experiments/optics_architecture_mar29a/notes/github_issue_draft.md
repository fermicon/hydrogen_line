# mar29a: 5 m optics architecture trade study

## Motivation
Choose a first-pass optical architecture for a 5 m student-built radio telescope that must support:
- H I at 1.420 GHz
- OH at 1.612 to 1.720 GHz
- H2O at 22.235 GHz

Simultaneous multiband observing is not required. The key question is whether the telescope should be prime focus or dual-reflector, and if a secondary is used, what diameter is defensible.

## Experiment
Run a compact trade study over three candidate architectures:
1. Prime-focus paraboloid with swappable feeds
2. On-axis classical Cassegrain
3. On-axis Gregorian only as a packaging sanity check

For the dual-reflector options, sweep subreflector diameter from 0.35 m to 0.95 m and evaluate:
- 22 GHz practicality
- low-band blockage cost
- feed/support complexity
- receiver placement
- alignment burden
- manufacturability by a student team
- upgrade path

## Desired measurement
Produce one main plot:
- x-axis: subreflector diameter
- y-axis: normalized architecture score
- curves: classical Cassegrain, oversized-secondary Cassegrain
- horizontal reference line: prime-focus baseline

Also include a compact table with:
- area blockage fraction
- nominal interpretation of each diameter regime

## Notes
Start from the smallest useful experiment. This is a design-screening sprint, not a full EM optimization. The output should be a crisp recommendation for Rev A plus a narrower size band if a secondary is mandatory.
