Summary:	Shim pytest plugin to enable celery.contrib.pytest
Summary(pl.UTF-8):	Minimalna wtyczka pytesta włączająca celery.contrib.pytest
Name:		python-pytest-celery
Version:	0.0.0
Release:	4
License:	BSD
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/pytest-celery/
Source0:	https://files.pythonhosted.org/packages/source/p/pytest-celery/pytest-celery-%{version}.tar.gz
# Source0-md5:	8ef15c46fe2da8ba836cde3ada776a7a
URL:		https://pypi.org/project/pytest-celery/
BuildRequires:	python-modules >= 1:2.5
BuildRequires:	python-setuptools
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
BuildRequires:	sed >= 4.0
Requires:	python-modules >= 1:2.5
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Shim pytest plugin to enable celery.contrib.pytest.

%description -l pl.UTF-8
Minimalna wtyczka pytesta włączająca celery.contrib.pytest.

%prep
%setup -q -n pytest-celery-%{version}

# change to setuptools to generate egg dependencies
%{__sed} -i -e 's,from distutils\.core,from setuptools,' setup.py

%build
%py_build

%install
rm -rf $RPM_BUILD_ROOT

%py_install

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE
%{py_sitescriptdir}/pytest_celery.py[co]
%{py_sitescriptdir}/pytest_celery-%{version}-py*.egg-info
