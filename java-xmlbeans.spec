# TODO:
# - use source package

%include	/usr/lib/rpm/macros.java
Summary:	XMLBeans is a technology for accessing XML by binding it to Java types
Name:		xmlbeans
Version:	2.4.0
Release:	0.1
License:	Apache v2.0
Group:		Development/Languages/Java
Source0:	http://apache.forall.pl/xmlbeans/binaries/%{name}-%{version}.zip
# Source0-md5:	43b92f83ad47f369035fc7b945e55b12
Patch0:		%{name}-classpath.patch
URL:		http://xmlbeans.apache.org/
BuildRequires:	jpackage-utils
BuildRequires:	rpm-javaprov
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	jpackage-utils
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
XMLBeans is a technology for accessing XML by binding it to Java
types. XMLBeans provides several ways to get at the XML, including:
- Through XML schema that has been compiled to generate Java types
  that represent schema types. In this way, you can access instances of
  the schema through JavaBeans-style accessors after the fashion of
  "getFoo" and "setFoo". The XMLBeans API also allows you to reflect
  into the XML schema itself through an XML Schema Object model.
- A cursor model through which you can traverse the full XML infoset.
- Support for XML DOM.

%package doc
Summary:	Manual for %{name}
Summary(fr.UTF-8):	Documentation pour %{name}
Summary(it.UTF-8):	Documentazione di %{name}
Summary(pl.UTF-8):	Podręcznik dla %{name}
Group:		Documentation

%description doc
Documentation for %{name}.

%description doc -l fr.UTF-8
Documentation pour %{name}.

%description doc -l it.UTF-8
Documentazione di %{name}.

%description doc -l pl.UTF-8
Dokumentacja do %{name}.

%prep
%setup -q

%patch0 -p1

rm bin/*.cmd
rm bin/_setlib

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_javadir}/xmlbeans,%{_bindir}}

cp lib/*.jar $RPM_BUILD_ROOT%{_javadir}/%{name}
ln -s %{name}/xbean.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
ln -s %{name}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar

install bin/* $RPM_BUILD_ROOT/%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_javadir}/%{name}
%{_javadir}/*.jar
%attr(755,root,root) %{_bindir}/*

%files doc
%defattr(644,root,root,755)
%doc docs/*
