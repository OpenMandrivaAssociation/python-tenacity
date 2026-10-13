Name:		python-tenacity
Version:	9.2.1
Release:	2
Summary:	Retry library for Python
License:	Apache-2.0
Group:		Development/Python
URL:		https://github.com/jd/tenacity
Source0:	https://files.pythonhosted.org/packages/source/t/tenacity/tenacity-%{version}.tar.gz
BuildArch:	noarch
BuildSystem:	python
BuildRequires:	pkgconfig(python3)
BuildRequires:	python%{pyver}dist(wheel)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(hatchling)
BuildRequires:	python%{pyver}dist(hatch-vcs)

%description
Tenacity is a general-purpose retrying library. It originates from a
fork of retrying and adds new functionality and bug fixes.

%build -p
# The sdist is not a git checkout, so the versioning backend needs the version.
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}

%files
%doc README.rst
%license LICENSE
%{py_sitedir}/tenacity
%{py_sitedir}/tenacity-*.*-info
