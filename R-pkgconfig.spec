#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-pkgconfig
Version  : 2.0.1
Release  : 12
URL      : https://cran.r-project.org/src/contrib/pkgconfig_2.0.1.tar.gz
Source0  : https://cran.r-project.org/src/contrib/pkgconfig_2.0.1.tar.gz
Summary  : Private Configuration for 'R' Packages
Group    : Development/Tools
License  : MIT
BuildRequires : clr-R-helpers

%description
Options set by a given package only apply to that package,
    other packages are unaffected.

%prep
%setup -q -c -n pkgconfig

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1509034843

%install
rm -rf %{buildroot}
export SOURCE_DATE_EPOCH=1509034843
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
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library pkgconfig
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library pkgconfig
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library pkgconfig|| : 
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/pkgconfig/DESCRIPTION
/usr/lib64/R/library/pkgconfig/INDEX
/usr/lib64/R/library/pkgconfig/LICENSE
/usr/lib64/R/library/pkgconfig/Meta/Rd.rds
/usr/lib64/R/library/pkgconfig/Meta/features.rds
/usr/lib64/R/library/pkgconfig/Meta/hsearch.rds
/usr/lib64/R/library/pkgconfig/Meta/links.rds
/usr/lib64/R/library/pkgconfig/Meta/nsInfo.rds
/usr/lib64/R/library/pkgconfig/Meta/package.rds
/usr/lib64/R/library/pkgconfig/NAMESPACE
/usr/lib64/R/library/pkgconfig/NEWS.markdown
/usr/lib64/R/library/pkgconfig/R/pkgconfig
/usr/lib64/R/library/pkgconfig/R/pkgconfig.rdb
/usr/lib64/R/library/pkgconfig/R/pkgconfig.rdx
/usr/lib64/R/library/pkgconfig/README.Rmd
/usr/lib64/R/library/pkgconfig/README.markdown
/usr/lib64/R/library/pkgconfig/help/AnIndex
/usr/lib64/R/library/pkgconfig/help/aliases.rds
/usr/lib64/R/library/pkgconfig/help/paths.rds
/usr/lib64/R/library/pkgconfig/help/pkgconfig.rdb
/usr/lib64/R/library/pkgconfig/help/pkgconfig.rdx
/usr/lib64/R/library/pkgconfig/html/00Index.html
/usr/lib64/R/library/pkgconfig/html/R.css
