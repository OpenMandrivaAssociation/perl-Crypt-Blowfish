%define module	Crypt-Blowfish
%define name	perl-%{module}
%define version 2.10
%define release %mkrel 3

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Perl Blowfish encryption module
License:	GPL or Artistic
Group:		Development/Perl
Source:		http://search.cpan.org/CPAN/authors/id/D/DP/DPARIS/%{module}-%{version}.tar.bz2
Url:            http://search.cpan.org/dist/%{module}/
Buildrequires:	 perl-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
Perl module to encrypt using the Blowfish algorithm.

%prep
%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%{__make} test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root)
%doc README COPYRIGHT Changes
%{perl_vendorarch}/Crypt
%{perl_vendorarch}/auto/Crypt
%{_mandir}/*/*

