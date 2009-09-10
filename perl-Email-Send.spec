#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Email
%define		pnam	Send
Summary:	Email::Send - simply sending email
Summary(pl.UTF-8):	Email::Send - po prostu wysyłanie e-maili
Name:		perl-Email-Send
Version:	2.198
Release:	1
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	a977d48219aaf21b8cfbefe2826bcd47
URL:		http://search.cpan.org/dist/Email-Send/
%if %{with tests}
BuildRequires:	perl-Email-Address >= 1.80
BuildRequires:	perl-Email-Simple >= 1.92
BuildRequires:	perl-Module-Pluggable >= 2.97
BuildRequires:	perl-Return-Value >= 1.28
%endif
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module provides a very simple, very clean, very specific
interface to multiple Email mailers. The goal if this software is to
be small and simple, easy to use, and easy to extend.

%description -l pl.UTF-8
Moduł ten dostarcza prostego, czystego i konkretnego interfejsu do
różnych programów pocztowych. W założeniach oprogramowanie to ma być
małe i proste, jak również łatwe w użyciu i rozszerzaniu.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Email/Send
%{perl_vendorlib}/Email/Send.pm
%{_mandir}/man3/*
