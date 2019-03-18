#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-survey
Version  : 3.35.1
Release  : 19
URL      : https://cran.r-project.org/src/contrib/survey_3.35-1.tar.gz
Source0  : https://cran.r-project.org/src/contrib/survey_3.35-1.tar.gz
Summary  : Analysis of Complex Survey Samples
Group    : Development/Tools
License  : GPL-2.0 GPL-3.0
Requires: R-DBI
Requires: R-bit64
Requires: R-blob
Requires: R-memoise
Requires: R-pkgconfig
BuildRequires : R-DBI
BuildRequires : R-RSQLite
BuildRequires : R-bit64
BuildRequires : R-blob
BuildRequires : R-memoise
BuildRequires : R-minqa
BuildRequires : R-numDeriv
BuildRequires : R-pkgconfig
BuildRequires : buildreq-R

%description
3stage2phase.R: twophase designs with three-stage sample at phase 1
api.R: Run example(api) to check that results haven't changed

%prep
%setup -q -c -n survey

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1552862942

%install
export SOURCE_DATE_EPOCH=1552862942
rm -rf %{buildroot}
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
R CMD check --no-manual --no-examples --no-codoc  survey || :


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
/usr/lib64/R/library/survey/tests/3stage2phase.R
/usr/lib64/R/library/survey/tests/DBIcheck.R
/usr/lib64/R/library/survey/tests/README
/usr/lib64/R/library/survey/tests/api.R
/usr/lib64/R/library/survey/tests/badcal.R
/usr/lib64/R/library/survey/tests/badcal.Rout.save
/usr/lib64/R/library/survey/tests/bycovmat.R
/usr/lib64/R/library/survey/tests/caleg.R
/usr/lib64/R/library/survey/tests/caleg.Rout.save
/usr/lib64/R/library/survey/tests/check.R
/usr/lib64/R/library/survey/tests/check.Rout.save
/usr/lib64/R/library/survey/tests/deff.R
/usr/lib64/R/library/survey/tests/deff.Rout.save
/usr/lib64/R/library/survey/tests/domain.R
/usr/lib64/R/library/survey/tests/domain.Rout.save
/usr/lib64/R/library/survey/tests/fpc.R
/usr/lib64/R/library/survey/tests/glm-scoping.R
/usr/lib64/R/library/survey/tests/kalton.R
/usr/lib64/R/library/survey/tests/kalton.Rout.save
/usr/lib64/R/library/survey/tests/lonely.psu.R
/usr/lib64/R/library/survey/tests/lonely.psu.Rout.save
/usr/lib64/R/library/survey/tests/multistage.R
/usr/lib64/R/library/survey/tests/nwtco-subcohort.rda
/usr/lib64/R/library/survey/tests/nwts-cch.R
/usr/lib64/R/library/survey/tests/nwts.R
/usr/lib64/R/library/survey/tests/nwts.Rout.save
/usr/lib64/R/library/survey/tests/nwts.rda
/usr/lib64/R/library/survey/tests/pps.R
/usr/lib64/R/library/survey/tests/quantile.R
/usr/lib64/R/library/survey/tests/quantile.Rout.save
/usr/lib64/R/library/survey/tests/rakecheck.R
/usr/lib64/R/library/survey/tests/rakecheck.Rout.save
/usr/lib64/R/library/survey/tests/raowuboot.R
/usr/lib64/R/library/survey/tests/raowuboot.Rout.save
/usr/lib64/R/library/survey/tests/regpredict.R
/usr/lib64/R/library/survey/tests/regpredict.Rout.save
/usr/lib64/R/library/survey/tests/scoping.R
/usr/lib64/R/library/survey/tests/simdata1.RData
/usr/lib64/R/library/survey/tests/survcurve.R
/usr/lib64/R/library/survey/tests/survcurve.Rout.save
/usr/lib64/R/library/survey/tests/testoutput/DBIcheck.R
/usr/lib64/R/library/survey/tests/testoutput/DBIcheck.Rout.save
/usr/lib64/R/library/survey/tests/testoutput/README
/usr/lib64/R/library/survey/tests/testoutput/api.R
/usr/lib64/R/library/survey/tests/testoutput/api.Rout.saved
/usr/lib64/R/library/survey/tests/testoutput/bycovmat.R
/usr/lib64/R/library/survey/tests/testoutput/bycovmat.Rout.save
/usr/lib64/R/library/survey/tests/testoutput/fpc.R
/usr/lib64/R/library/survey/tests/testoutput/fpc.Rout.save
/usr/lib64/R/library/survey/tests/testoutput/multistage.R
/usr/lib64/R/library/survey/tests/testoutput/multistage.Rout.save
/usr/lib64/R/library/survey/tests/testoutput/nwtco-subcohort.rda
/usr/lib64/R/library/survey/tests/testoutput/nwts-cch.R
/usr/lib64/R/library/survey/tests/testoutput/nwts-cch.Rout.save
/usr/lib64/R/library/survey/tests/testoutput/nwts.rda
/usr/lib64/R/library/survey/tests/testoutput/pps.R
/usr/lib64/R/library/survey/tests/testoutput/pps.Rout.save
/usr/lib64/R/library/survey/tests/testoutput/scoping.R
/usr/lib64/R/library/survey/tests/testoutput/scoping.Rout.save
/usr/lib64/R/library/survey/tests/twophase.R
/usr/lib64/R/library/survey/tests/twophase.Rout.save
/usr/lib64/R/library/survey/twostage.pdf
/usr/lib64/R/library/survey/ucla-examples.pdf
