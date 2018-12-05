#! /bin/csh -f

#===========================================================
# Ensure all script arguments are passed from command line
#===========================================================
if ($#argv != 1) then
    echo "=== You must give exactly 1 argument; The directory you want to copy"
    echo "\n=== For example:"
    echo "./getPublicCERN.csh Combine"
    echo
    exit 1
endif

set DIR     = ${1}
set ADDRESS = "attikis@lxplus.cern.ch:~/public/html/${DIR}"
set RSYNC   = "rsync -r --partial --progress "
set CMD     = "${RSYNC} ${ADDRESS} ."

echo "=== Executing: ${CMD}"
$CMD
