#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Email
%define	pnam	Send
Summary:	Email::Send - simply sending email
Summary(pl):	Email::Send - po prostu wysy�anie e-maili
Name:		perl-Email-Send
Version:	1.43
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	ad5b0d6ba14493991896e6ad4fbe1448
URL:		http://search.cpan.org/dist/Email-Send/
%if %{with tests}
BuildRequires:	perl-Email-Address
BuildRequires:	perl-Email-Simple
%endif
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module provides a very simple, very clean, very specific
interface to multiple Email mailers. The goal if this software is to
be small and simple, easy to use, and easy to extend.

%description -l pl
Modu� ten dostarcza prostego, czystego i konkretnego interfejsu do
r�nych program�w pocztowych. W za�o�eniach oprogramowanie to ma by�
ma�e i proste, jak r�wnie� �atwe w u�yciu i rozszerzaniu.

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
