Name:		python-tenacity
Version:	9.1.4
Release:	1
Summary:	Retry library for Python
License:	Apache-2.0
Group:		Development/Python
URL:		https://github.com/jd/tenacity
Source0:	https://files.pythonhosted.org/packages/source/t/tenacity/tenacity-%{version}.tar.gz
BuildArch:	noarch
BuildSystem:	python
BuildRequires:	python
BuildRequires:	pkgconfig(python)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(setuptools-scm)
BuildRequires:	python%{pyver}dist(wheel)

%description
Tenacity is a general-purpose retrying library. It originates from a
fork of retrying and adds new functionality and bug fixes.

%files
%doc README.rst
%license LICENSE
%{py_sitedir}/tenacity
%{py_sitedir}/tenacity-*.*-info
