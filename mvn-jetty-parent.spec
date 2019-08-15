#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : mvn-jetty-parent
Version  : 8
Release  : 6
URL      : https://github.com/eclipse/jetty.parent/archive/jetty-parent-8.tar.gz
Source0  : https://github.com/eclipse/jetty.parent/archive/jetty-parent-8.tar.gz
Source1  : https://repo1.maven.org/maven2/org/eclipse/jetty/jetty-parent/11/jetty-parent-11.pom
Source2  : https://repo1.maven.org/maven2/org/eclipse/jetty/jetty-parent/14/jetty-parent-14.pom
Source3  : https://repo1.maven.org/maven2/org/eclipse/jetty/jetty-parent/17/jetty-parent-17.pom
Source4  : https://repo1.maven.org/maven2/org/eclipse/jetty/jetty-parent/18/jetty-parent-18.pom
Source5  : https://repo1.maven.org/maven2/org/eclipse/jetty/jetty-parent/23/jetty-parent-23.pom
Source6  : https://repo1.maven.org/maven2/org/eclipse/jetty/jetty-parent/25/jetty-parent-25.pom
Source7  : https://repo1.maven.org/maven2/org/mortbay/jetty/jetty-parent/10/jetty-parent-10.pom
Source8  : https://repo1.maven.org/maven2/org/mortbay/jetty/jetty-parent/7/jetty-parent-7.pom
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0 EPL-1.0
Requires: mvn-jetty-parent-data = %{version}-%{release}

%description
No detailed description available

%package data
Summary: data components for the mvn-jetty-parent package.
Group: Data

%description data
data components for the mvn-jetty-parent package.


%prep
%setup -q -n jetty.parent-jetty-parent-8

%build

%install
mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/eclipse/jetty/jetty-parent/11
cp %{SOURCE1} %{buildroot}/usr/share/java/.m2/repository/org/eclipse/jetty/jetty-parent/11/jetty-parent-11.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/eclipse/jetty/jetty-parent/14
cp %{SOURCE2} %{buildroot}/usr/share/java/.m2/repository/org/eclipse/jetty/jetty-parent/14/jetty-parent-14.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/eclipse/jetty/jetty-parent/17
cp %{SOURCE3} %{buildroot}/usr/share/java/.m2/repository/org/eclipse/jetty/jetty-parent/17/jetty-parent-17.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/eclipse/jetty/jetty-parent/18
cp %{SOURCE4} %{buildroot}/usr/share/java/.m2/repository/org/eclipse/jetty/jetty-parent/18/jetty-parent-18.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/eclipse/jetty/jetty-parent/23
cp %{SOURCE5} %{buildroot}/usr/share/java/.m2/repository/org/eclipse/jetty/jetty-parent/23/jetty-parent-23.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/eclipse/jetty/jetty-parent/25
cp %{SOURCE6} %{buildroot}/usr/share/java/.m2/repository/org/eclipse/jetty/jetty-parent/25/jetty-parent-25.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/mortbay/jetty/jetty-parent/10
cp %{SOURCE7} %{buildroot}/usr/share/java/.m2/repository/org/mortbay/jetty/jetty-parent/10/jetty-parent-10.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/mortbay/jetty/jetty-parent/7
cp %{SOURCE8} %{buildroot}/usr/share/java/.m2/repository/org/mortbay/jetty/jetty-parent/7/jetty-parent-7.pom


%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/java/.m2/repository/org/eclipse/jetty/jetty-parent/11/jetty-parent-11.pom
/usr/share/java/.m2/repository/org/eclipse/jetty/jetty-parent/14/jetty-parent-14.pom
/usr/share/java/.m2/repository/org/eclipse/jetty/jetty-parent/17/jetty-parent-17.pom
/usr/share/java/.m2/repository/org/eclipse/jetty/jetty-parent/18/jetty-parent-18.pom
/usr/share/java/.m2/repository/org/eclipse/jetty/jetty-parent/23/jetty-parent-23.pom
/usr/share/java/.m2/repository/org/eclipse/jetty/jetty-parent/25/jetty-parent-25.pom
/usr/share/java/.m2/repository/org/mortbay/jetty/jetty-parent/10/jetty-parent-10.pom
/usr/share/java/.m2/repository/org/mortbay/jetty/jetty-parent/7/jetty-parent-7.pom
