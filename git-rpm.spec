Name:		git-rpm
Version:	1.00
Release:	1%{?dist}
Summary:	RPM Build Support Tool

Group:		Development/Tools
License:	GPL+ or Artistic
URL:		http://qiita.com/ymko
Source0:	%{name}-%{version}.tar.gz
BuildArch:	noarch
AutoReqProv:	no

%description

%prep
%setup -q -a 0

%install
install -d ${RPM_BUILD_ROOT}/%{_bindir}
install -m 755 git-rpm ${RPM_BUILD_ROOT}/%{_bindir}/git-rpm

%files
%{_bindir}/*

%changelog
* Sat Jan 17 2015 ymko <ymko@example.com> - 1.00-1
- First Release

