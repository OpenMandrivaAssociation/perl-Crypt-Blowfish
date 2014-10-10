%define modname	Crypt-Blowfish
%define modver 2.14

Summary:	Perl Blowfish encryption module
Name:		perl-%{modname}
Version:	%perl_convert_version %{modver}
Release:	5
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{modname}/
Source0:	http://www.cpan.org/authors/id/D/DP/DPARIS/Crypt-Blowfish-%{modver}.tar.gz
Buildrequires:	perl-devel

%description
Perl module to encrypt using the Blowfish algorithm.

%prep
%setup -qn %{modname}-%{modver}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc README COPYRIGHT Changes
%{perl_vendorarch}/Crypt
%{perl_vendorarch}/auto/Crypt
%{_mandir}/man3/*


