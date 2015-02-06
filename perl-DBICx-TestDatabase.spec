%define upstream_name    DBICx-TestDatabase
%define upstream_version 0.05

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	5

Summary:	A DBICx::TestDatabase you can add your 
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/DBICx/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(DBD::SQLite)
BuildRequires:	perl(DBIx::Class)
BuildRequires:	perl(File::Temp)
BuildRequires:	perl(SQL::Translator)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(ok)
BuildRequires:	perl(strictures)
BuildArch:	noarch

%description
This module creates a temporary SQLite database, deploys your DBIC schema,
and then connects to it. This lets you easily test your DBIC schema. Since
you have a fresh database for every test, you don't have to worry about
cleaning up after your tests, ordering of tests affecting failure, etc.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc README Changes
%{_mandir}/man3/*
%{perl_vendorlib}/*
