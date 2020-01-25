#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define		pdir	Net
%define		pnam	IDN-IDNA2003
Summary:	Net::IDN::IDNA2003 - Internationalizing Domain Names in Applications (2003) (RFC 3490)
Summary(pl.UTF-8):	Net::IDN::IDNA2003 - międzynarodowe nazwy domen (IDN) w aplikacjach (2003) (RFC 3490)
Name:		perl-Net-IDN-IDNA2003
Version:	1.000
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Net/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	ff14b5276766205910942741aef387f1
URL:		http://search.cpan.org/dist/Net-IDN-IDNA2003/
BuildRequires:	perl-Module-Build
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Net-IDN-Encode >= 1
BuildRequires:	perl-Net-IDN-Nameprep >= 1.100
BuildRequires:	perl-Test-NoWarnings
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module implements the original IDNA standard defined in RFC 3490
and related documents (IDNA2003). You should use this module if you
want an exact implementation of the original IDNA specification.

However, if you just want to convert domain names and don't care which
standard is used internally, you should use Net::IDN::Encode instead.

%description -l pl.UTF-8
Ten moduł implementuje oryginalny standard IDNA zdefiniowany w RFC 3490
i powiązanych dokumentach (IDNA2003). Należy go używać, jeśli
potrzebujemy dokładnej implementacji oryginalnej specyfikacji IDNA.

Jeśli jednak chcemy konwertować nazwy domen bez zwracania uwagi na
używany wewnętrznie standard, należy używać Net::IDN::Encode.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Build.PL \
	destdir=$RPM_BUILD_ROOT \
	installdirs=vendor
./Build

%{?with_tests:./Build test}

%install
rm -rf $RPM_BUILD_ROOT

./Build install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Net/IDN/IDNA2003.pm
%{_mandir}/man3/Net::IDN::IDNA2003.3pm*
