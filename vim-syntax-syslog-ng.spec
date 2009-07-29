%define		syntax	syslog-ng
%define		ver		3.0.2
Summary:	Vim syntax: %{syntax}
Name:		vim-syntax-%{syntax}
Version:	1.5.5a
Release:	1
License:	GPL v2
Group:		Applications/Editors/Vim
Source0:	http://www.balabit.com/downloads/files/syslog-ng/sources/%{version}/source/%{syntax}_%{ver}.tar.gz
# Source0-md5:	0dce90ddd4f0f417ce2b9d88ccbca2e9
Source1:	ftdetect.vim
# for _vimdatadir existence
Requires:	vim-rt >= 4:6.3.058-3
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_vimdatadir	%{_datadir}/vim/vimfiles

%description
This plugin provides syntax highlighting for syslog-ng config files.

%prep
%setup -qc
mv %{syntax}-%{ver}/contrib/*.vim .

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_vimdatadir}/{syntax,ftdetect}
cp -a syslog-ng.vim $RPM_BUILD_ROOT%{_vimdatadir}/syntax/%{syntax}.vim
cp -a %{SOURCE1} $RPM_BUILD_ROOT%{_vimdatadir}/ftdetect/%{syntax}.vim

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_vimdatadir}/syntax/%{syntax}.vim
%{_vimdatadir}/ftdetect/%{syntax}.vim
