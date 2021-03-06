# TODO:
# - use source package
# - There is no spec for:
#   java-xom (http://www.cafeconleche.org/XOM/)
#   java-stax (http://stax.codehaus.org/)
# - maven data (needed for xmlbeansxx.spec)

%define		srcname	xmlbeans
Summary:	XMLBeans is a technology for accessing XML by binding it to Java types
Name:		java-xmlbeans
Version:	2.4.0
Release:	0.1
License:	Apache v2.0
Group:		Libraries/Java
Source0:	http://www.apache.org/dist/xmlbeans/source/xmlbeans-%{version}-src.zip
# Source0-md5:	d6fc091ac3b435babdacf92d277ab3bf
# based on https://saxon.svn.sourceforge.net/svnroot/saxon/latest9.1/build/build.xml
Source1:	%{name}-build.xml
Patch0:		%{srcname}-classpath.patch
URL:		http://xmlbeans.apache.org/
BuildRequires:	ant
BuildRequires:	ant-nodeps
BuildRequires:	dom4j
BuildRequires:	java-stax
BuildRequires:	java-xom
BuildRequires:	jdom
BuildRequires:	jpackage-utils
BuildRequires:	rpm-javaprov
BuildRequires:	rpmbuild(macros) >= 1.300
BuildRequires:	unzip
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
Summary:	Manual for %{srcname}
Summary(fr.UTF-8):	Documentation pour %{srcname}
Summary(it.UTF-8):	Documentazione di %{srcname}
Summary(pl.UTF-8):	Podręcznik dla %{srcname}
Group:		Documentation

%description doc
Documentation for %{srcname}.

%description doc -l fr.UTF-8
Documentation pour %{srcname}.

%description doc -l it.UTF-8
Documentazione di %{srcname}.

%description doc -l pl.UTF-8
Dokumentacja do %{srcname}.

%prep
%setup -q -n %{srcname}-%{version}

%patch0 -p1

rm bin/*.cmd
rm bin/_setlib

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_javadir}/xmlbeans,%{_bindir}}

cp lib/*.jar $RPM_BUILD_ROOT%{_javadir}/%{srcname}
ln -s %{srcname}/xbean.jar $RPM_BUILD_ROOT%{_javadir}/%{srcname}-%{version}.jar
ln -s %{srcname}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{srcname}.jar

install bin/* $RPM_BUILD_ROOT/%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_javadir}/%{srcname}
%{_javadir}/*.jar
%attr(755,root,root) %{_bindir}/*

%files doc
%defattr(644,root,root,755)
%doc docs/*
