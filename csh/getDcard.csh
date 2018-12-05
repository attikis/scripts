#! /bin/csh -f
  if ($#argv != 1) then
        echo "Usage: $0 <pseudo-milticrab>"
        echo "Copies <pseudo-milticrab> from FNAL LPC machine locally"
        goto done
    endif

# Save command line args in variables
set MCRAB=$1

set WORKPATH=/uscms_data/d3/aattikis/workspace/cmssw/CMSSW_8_0_30/src/HiggsAnalysis/NtupleAnalysis/src/LimitCalc/work
#set WORKPATH=/publicweb/a/aattikis/
rsync --partial --progress -r aattikis@cmslpc-sl6.fnal.gov:${WORKPATH}/${MCRAB} .
