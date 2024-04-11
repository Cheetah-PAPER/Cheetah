# Cheetah focus on group-update mining.

Cheetah generates Explore-Domains from the initial graph matches (mined using GraphPi https://github.com/thu-pacman/GraphPi), then executes group-update mining with the Explore-Domains and the inputed updates:

$ ./TC -inigraph ../inputs/wikitalk/inigraph -streamPath ../inputs/wikitalk/[edge streams file] -outputFile /tmp/output/tc\_log ../inputs/wikitalk/[explore-domains file]

$ ./CF -inigraph ../inputs/wikitalk/inigraph -streamPath ../inputs/wikitalk/[edge streams file] -outputFile /tmp/output/cf\_log ../inputs/wikitalk/[explore-domains file]

$ ./MC -inigraph ../inputs/wikitalk/inigraph -streamPath ../inputs/wikitalk/[edge streams file] -outputFile /tmp/output/mc\_log ../inputs/wikitalk/[explore-domains file]

$ ./FSM -inigraph ../inputs/wikitalk/inigraph -streamPath ../inputs/wikitalk/[edge streams file] -outputFile /tmp/output/fsm\_log ../inputs/wikitalk/[explore-domains file]

