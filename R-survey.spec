#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-survey
Version  : 3.33.2
Release  : 1
URL      : https://cran.r-project.org/src/contrib/survey_3.33-2.tar.gz
Source0  : https://cran.r-project.org/src/contrib/survey_3.33-2.tar.gz
Summary  : Analysis of Complex Survey Samples
Group    : Development/Tools
License  : GPL-2.0 GPL-3.0
Requires: R-RSQLite
BuildRequires : R-RSQLite
BuildRequires : clr-R-helpers

%description
api.R: Run example(api) to check that results haven't changed
bycovmat.R: Check that svyby(,covmat=TRUE) is getting the ordering
of estimates correct.

%prep
%setup -q -c -n survey

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1521182855

%install
rm -rf %{buildroot}
export SOURCE_DATE_EPOCH=1521182855
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library survey
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library survey
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library survey
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library survey|| : 
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/survey/BUGS
/usr/lib64/R/library/survey/CITATION
/usr/lib64/R/library/survey/COPYING
/usr/lib64/R/library/survey/DESCRIPTION
/usr/lib64/R/library/survey/INDEX
/usr/lib64/R/library/survey/Meta/Rd.rds
/usr/lib64/R/library/survey/Meta/data.rds
/usr/lib64/R/library/survey/Meta/features.rds
/usr/lib64/R/library/survey/Meta/hsearch.rds
/usr/lib64/R/library/survey/Meta/links.rds
/usr/lib64/R/library/survey/Meta/nsInfo.rds
/usr/lib64/R/library/survey/Meta/package.rds
/usr/lib64/R/library/survey/Meta/vignette.rds
/usr/lib64/R/library/survey/NAMESPACE
/usr/lib64/R/library/survey/NEWS
/usr/lib64/R/library/survey/R/survey
/usr/lib64/R/library/survey/R/survey.rdb
/usr/lib64/R/library/survey/R/survey.rdx
/usr/lib64/R/library/survey/R/sysdata.rdb
/usr/lib64/R/library/survey/R/sysdata.rdx
/usr/lib64/R/library/survey/api.db
/usr/lib64/R/library/survey/data/api.rda
/usr/lib64/R/library/survey/data/crowd.rda
/usr/lib64/R/library/survey/data/election.rda
/usr/lib64/R/library/survey/data/fpc.rda
/usr/lib64/R/library/survey/data/hospital.rda
/usr/lib64/R/library/survey/data/mu284.rda
/usr/lib64/R/library/survey/data/nhanes.rda
/usr/lib64/R/library/survey/data/scd.rda
/usr/lib64/R/library/survey/data/yrbs.rda
/usr/lib64/R/library/survey/disclaimer
/usr/lib64/R/library/survey/doc/domain.R
/usr/lib64/R/library/survey/doc/domain.Rnw
/usr/lib64/R/library/survey/doc/domain.pdf
/usr/lib64/R/library/survey/doc/epi.R
/usr/lib64/R/library/survey/doc/epi.Rnw
/usr/lib64/R/library/survey/doc/epi.pdf
/usr/lib64/R/library/survey/doc/index.html
/usr/lib64/R/library/survey/doc/nwtco-subcohort.rda
/usr/lib64/R/library/survey/doc/nwts.rda
/usr/lib64/R/library/survey/doc/phase1.R
/usr/lib64/R/library/survey/doc/phase1.Rnw
/usr/lib64/R/library/survey/doc/phase1.pdf
/usr/lib64/R/library/survey/doc/pps.R
/usr/lib64/R/library/survey/doc/pps.Rnw
/usr/lib64/R/library/survey/doc/pps.pdf
/usr/lib64/R/library/survey/doc/survey.R
/usr/lib64/R/library/survey/doc/survey.Rnw
/usr/lib64/R/library/survey/doc/survey.pdf
/usr/lib64/R/library/survey/help/AnIndex
/usr/lib64/R/library/survey/help/aliases.rds
/usr/lib64/R/library/survey/help/paths.rds
/usr/lib64/R/library/survey/help/survey.rdb
/usr/lib64/R/library/survey/help/survey.rdx
/usr/lib64/R/library/survey/html/00Index.html
/usr/lib64/R/library/survey/html/R.css
/usr/lib64/R/library/survey/porting.to.S
/usr/lib64/R/library/survey/twostage.pdf
/usr/lib64/R/library/survey/ucla-examples.pdf
