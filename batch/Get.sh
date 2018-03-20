#!/bin/bash
#PBS -S /bin/bash
#PBS -l walltime=24:00:00
#PBS -l pmem=1gb


STARTTIME=`date +%s`
date

echo 
echo "Environment variables..."
echo " User name:     $USER"
echo " User home:     $HOME"
echo " Queue name:    $PBS_O_QUEUE"
echo " Job name:      $PBS_JOBNAME"
echo " Job-id:        $PBS_JOBID"
echo " Work dir:      $PBS_O_WORKDIR"
echo " Submit host:   $PBS_O_HOST"
echo " Worker node:   $HOSTNAME"
#echo " Temp dir:      $TMPDIR"
echo " parameters passed: $*"
echo 


echo " Temp dir:      $JOBTMP"

echo " SCRIPT:        $SCRIPT"
echo " TREEFILE:      $TREEFILE"
echo " METAFILE:      $METAFILE"
echo " CUTFLOWFILE:   $CUTFLOWFILE"
echo " MERGEDTREE:    $MERGEDTREE"
echo " MERGEDMETA:    $MERGEDMETA"
echo " MERGEDCUTFLOW: $MERGEDCUTFLOW"
echo " OUTTREE:       $OUTTREE"
echo " OUTMETA:       $OUTMETA"
echo " OUTCUTFLOW:    $OUTCUTFLOW"
echo " MERGED:        $MERGED"
echo " OUTMERGED:     $OUTMERGED"
echo " NCORES:        $NCORES"

echo
export 

MYDIR=Get_${RANDOM}${RANDOM}

# ----------------
# This is the job!
# ----------------

export X509_USER_PROXY=/coepp/cephfs/mel/fscutti/jobdir/x509up_u1132
setupATLAS

# -----------------------------
# avoid to fuck the cluster up:
# -----------------------------


cgcreate -a ${USER}:people -t ${USER}:people -g cpu,memory:user/${USER}/${PBS_JOBID}
MEMLIMIT="$((3 * ${NCORES}))"
echo "${MEMLIMIT}g" > /cgroup/memory/user/${USER}/${PBS_JOBID}/memory.limit_in_bytes
echo $$ > /cgroup/memory/user/${USER}/${PBS_JOBID}/tasks


echo "executing job..."

#echo "-----> ls ${JOBTMP} -la"
#ls ${JOBTMP} -la

#echo "-----> rm -rf ${MYDIR}"
#rm -rf ${MYDIR}

#echo "-----> rm -rf *.root"
#rm -rf *.root

#echo "-----> ls ${JOBTMP} -la"
#ls ${JOBTMP} -la

echo "-----> mkdir ${JOBTMP}/${MYDIR} "
mkdir ${JOBTMP}/${MYDIR} 

echo "-----> ls ${JOBTMP} -la"
ls ${JOBTMP} -la


# -------------------
# download with rucio
# -------------------
lsetup rucio

# tree file
# ---------
echo "-----> rucio download --dir=${JOBTMP}/${MYDIR} ${TREEFILE}"
rucio download --dir=${JOBTMP}/${MYDIR} ${TREEFILE}

echo "-----> ls ${JOBTMP}/${MYDIR}/${TREEFILE} -la"
ls ${JOBTMP}/${MYDIR}/${TREEFILE} -la

echo "-----> cp -rf ${JOBTMP}/${MYDIR}/${TREEFILE} ${OUTTREE}"
cp -rf ${JOBTMP}/${MYDIR}/${TREEFILE} ${OUTTREE}

# meta file
# ---------
echo "-----> rucio download --dir=${JOBTMP}/${MYDIR} ${METAFILE}"
rucio download --dir=${JOBTMP}/${MYDIR} ${METAFILE}

echo "-----> ls ${JOBTMP}/${MYDIR}/${METAFILE} -la"
ls ${JOBTMP}/${MYDIR}/${METAFILE} -la

echo "-----> cp -rf ${JOBTMP}/${MYDIR}/${METAFILE} ${OUTMETA}"
cp -rf ${JOBTMP}/${MYDIR}/${METAFILE} ${OUTMETA}

# cutflow file
# ------------
echo "-----> rucio -v get --dir=${JOBTMP}/${MYDIR} ${CUTFLOWFILE}"
rucio -v get --dir=${JOBTMP}/${MYDIR} ${CUTFLOWFILE}

echo "-----> ls ${JOBTMP}/${MYDIR}/${CUTFLOWFILE} -la"
ls ${JOBTMP}/${MYDIR}/${CUTFLOWFILE} -la

echo "-----> cp -rf ${JOBTMP}/${MYDIR}/${CUTFLOWFILE} ${OUTCUTFLOW}"
cp -rf ${JOBTMP}/${MYDIR}/${CUTFLOWFILE} ${OUTCUTFLOW}





# --------------
# hadd with root
# --------------
lsetup root

# tree file
# ---------
echo "-----> cd ${JOBTMP}/${MYDIR}/${TREEFILE}"
cd ${JOBTMP}/${MYDIR}/${TREEFILE}

echo "-----> hadd ${MERGEDTREE} *.root*"
hadd ${MERGEDTREE} *.root*

echo "-----> cp ${MERGEDTREE} ${JOBTMP}/${MYDIR}"
cp ${MERGEDTREE} ${JOBTMP}/${MYDIR}

echo "-----> cd ${JOBTMP}/${MYDIR}"
cd ${JOBTMP}/${MYDIR}

echo "-----> rm -rf ${JOBTMP}/${MYDIR}/${TREEFILE}"
rm -rf ${JOBTMP}/${MYDIR}/${TREEFILE}

echo "-----> ls ${JOBTMP}/${MYDIR} -la"
ls ${JOBTMP}/${MYDIR} -la


# meta file
# ---------
echo "-----> cd ${JOBTMP}/${MYDIR}/${CUTFLOWFILE}"
cd ${JOBTMP}/${MYDIR}/${CUTFLOWFILE}

echo "-----> hadd ${MERGEDCUTFLOW} *.root*"
hadd ${MERGEDCUTFLOW} *.root*

echo "-----> cp ${MERGEDCUTFLOW} ${JOBTMP}/${MYDIR}"
cp ${MERGEDCUTFLOW} ${JOBTMP}/${MYDIR}

echo "-----> cd ${JOBTMP}/${MYDIR}"
cd ${JOBTMP}/${MYDIR}

echo "-----> rm -rf ${JOBTMP}/${MYDIR}/${CUTFLOWFILE}"
rm -rf ${JOBTMP}/${MYDIR}/${CUTFLOWFILE}

echo "-----> ls ${JOBTMP}/${MYDIR} -la"
ls ${JOBTMP}/${MYDIR} -la


# cutflow file
# ------------
echo "-----> cd ${JOBTMP}/${MYDIR}/${METAFILE}"
cd ${JOBTMP}/${MYDIR}/${METAFILE}

echo "-----> hadd ${MERGEDMETA} *.root*"
hadd ${MERGEDMETA} *.root*

echo "-----> cp ${MERGEDMETA} ${JOBTMP}/${MYDIR}"
cp ${MERGEDMETA} ${JOBTMP}/${MYDIR}

echo "-----> cd ${JOBTMP}/${MYDIR}"
cd ${JOBTMP}/${MYDIR}

echo "-----> rm -rf ${JOBTMP}/${MYDIR}/${METAFILE}"
rm -rf ${JOBTMP}/${MYDIR}/${METAFILE}

echo "-----> ls ${JOBTMP}/${MYDIR} -la"
ls ${JOBTMP}/${MYDIR} -la



# ----------------------
# merge cutflow and tree
# ----------------------
echo "-----> hadd ${MERGED} ${MERGEDTREE} ${MERGEDMETA} ${MERGEDCUTFLOW}"
hadd ${MERGED} ${MERGEDTREE} ${MERGEDMETA} ${MERGEDCUTFLOW}

echo "-----> ls ${JOBTMP}/${MYDIR} -la"
ls ${JOBTMP}/${MYDIR} -la

echo "-----> cp ${MERGED} ${OUTMERGED}"
cp ${MERGED} ${OUTMERGED}

echo "-----> cd ${JOBTMP}"
cd ${JOBTMP}

echo "-----> rm -rf ${MYDIR}"
rm -rf ${MYDIR}

echo "-----> ls ${JOBTMP} -la"
ls ${JOBTMP} -la

# EOF

