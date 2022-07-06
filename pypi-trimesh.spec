#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-trimesh
Version  : 3.12.7
Release  : 7
URL      : https://files.pythonhosted.org/packages/43/51/4839b99bc43c8bc22f60283e9a37671c79339807500b3e4988b8d4962d70/trimesh-3.12.7.tar.gz
Source0  : https://files.pythonhosted.org/packages/43/51/4839b99bc43c8bc22f60283e9a37671c79339807500b3e4988b8d4962d70/trimesh-3.12.7.tar.gz
Summary  : Import, export, process, analyze and view triangular meshes.
Group    : Development/Tools
License  : MIT
Requires: pypi-trimesh-license = %{version}-%{release}
Requires: pypi-trimesh-python = %{version}-%{release}
Requires: pypi-trimesh-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(numpy)
BuildRequires : pypi(setuptools)
BuildRequires : pypi(wheel)

%description
[![trimesh](https://trimsh.org/images/logotype-a.svg)](http://trimsh.org)
-----------
[![Github Actions](https://github.com/mikedh/trimesh/workflows/Release%20Trimesh/badge.svg)](https://github.com/mikedh/trimesh/actions)  [![PyPI version](https://badge.fury.io/py/trimesh.svg)](https://badge.fury.io/py/trimesh) [![codecov](https://codecov.io/gh/mikedh/trimesh/branch/main/graph/badge.svg?token=4PVRQXyl2h)](https://codecov.io/gh/mikedh/trimesh)

%package license
Summary: license components for the pypi-trimesh package.
Group: Default

%description license
license components for the pypi-trimesh package.


%package python
Summary: python components for the pypi-trimesh package.
Group: Default
Requires: pypi-trimesh-python3 = %{version}-%{release}

%description python
python components for the pypi-trimesh package.


%package python3
Summary: python3 components for the pypi-trimesh package.
Group: Default
Requires: python3-core
Provides: pypi(trimesh)
Requires: pypi(numpy)

%description python3
python3 components for the pypi-trimesh package.


%prep
%setup -q -n trimesh-3.12.7
cd %{_builddir}/trimesh-3.12.7
pushd ..
cp -a trimesh-3.12.7 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1657130489
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 -msse2avx"
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 -msse2avx "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -m build --wheel --skip-dependency-check --no-isolation

popd

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-trimesh
cp %{_builddir}/trimesh-3.12.7/LICENSE.md %{buildroot}/usr/share/package-licenses/pypi-trimesh/4340a750e3e91283c3d07c3eebda208f9e666c0b
pip install --root=%{buildroot} --no-deps --ignore-installed dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
pip install --root=%{buildroot}-v3 --no-deps --ignore-installed dist/*.whl
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-trimesh/4340a750e3e91283c3d07c3eebda208f9e666c0b

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
