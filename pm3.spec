Summary:	Polytechnique Montreal Modula-3
Name:		pm3
Version:	1.1.13
Release:	1
Copyright:	free
Group:		Development/Languages
Group(pl):	Programowanie/Jêzyki
Source:		ftp://m3.polymtl.ca/pub/m3/targzip/%{name}-%{version}-src.tgz
Patch:		pm3-debian.patch
Requires:	libpm3 = %{version}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Modula-3 distribution of Ecole Polytechnique de Montreal is based
on the DEC SRC Modula-3 programming environment.

Modula-3 is a systems programming language that descends from Mesa,
Modula-2, Cedar, and Modula-2+. It also resembles its cousins Object
Pascal, Oberon, and Euclid.

The goal of Modula-3 is to be as simple and safe as it can be while
meeting the needs of modern systems programmers. Instead of exploring new
features, they studied the features of the Modula family of languages
that have proven themselves in practice and tried to simplify them into
a harmonious language. They found that most of the successful features
were aimed at one of two main goals: greater robustness, and a simpler,
more systematic type system.

Modula-3 retains one of Modula-2's most successful features, the
provision for explicit interfaces between modules. It adds objects and
classes, exception handling, garbage collection, lightweight processes
(or threads), and the isolation of unsafe features.

A large number of platform independent libraries are available for easily
constructing distributed, graphical, multi-threaded applications.

%package extra
Summary:	Polytechnique Montreal Modula-3 Extra Files
Group:		Development/Languages
Group(pl):	Programowanie/Jêzyki
Requires:	%{name} = %{version}

%description extra
The Modula-3 distribution of Ecole Polytechnique de Montreal is based
on the DEC SRC Modula-3 programming environment.  This package contains
tools and demonstrations not actually part of the base compiler itself, but
nonetheless probably very useful for Modula-3 development.

%package -n libpm3
Summary:	Polytechnique Montreal Modula-3 Libraries.
Group:		Libraries
Group(pl):	Biblioteki

%description -n libpm3
The Modula-3 distribution of Ecole Polytechnique de Montreal is based
on the DEC SRC Modula-3 programming environment.  Programs built with
PM3 require this library.

%package -n libpm3-extra
Summary:	Polytechnique Montreal Modula-3 Extra Libraries
Group:		Libraries
Group(pl):	Biblioteki
Requires:	libpm3 = %{version}

%description -n libpm3-extra
The Modula-3 distribution of Ecole Polytechnique de Montreal is based
on the DEC SRC Modula-3 programming environment.  This package contains
libraries not actually part of the base compiler itself, but nonetheless
probably very useful for Modula-3 development.

%package -n libpm3-static
Summary:	Polytechnique Montreal Modula-3 Static Libraries.
Group:		Development/Libraries
Group(pl):	Programowanie/Biblioteki
Requires:	libpm3 = %{version}

%description -n libpm3-static
The Modula-3 distribution of Ecole Polytechnique de Montreal is based
on the DEC SRC Modula-3 programming environment.  This package contains
the static link libraries needed to build standalone executables.

%package -n m3gdb
Summary:	Modula-3 aware debugger based on GDB.
Group:		Development/Debuggers
Group(pl):	Programowanie/Odpluskwiacze
Requires:	%{name} = %{version}

%description -n m3gdb
GDB is a source-level debugger, capable of breaking programs at any specific
line, displaying variable values, and determining where errors occurred.
This is a special version of GDB which can be used to debug programs built
with Modula-3.  It is probably not as current as the standard GDB, so you
won't likely want this unless you are using PM3.

%package -n obliq
Summary:	An interactive interpreter for the Obliq language.
Group:		Development/Languages
Group(pl):	Programowanie/Jêzyki
Requires:	libpm3 = %{version}
Requires:	libpm3-extra = %{version}

%description -n obliq
Obliq is a small, statically scoped, untyped language. It is object-oriented,
higher-order, and distributed. State is local to an address space, while
computation can migrate over the network. The distributed computation
mechanism is based on Modula-3 Network Objects.

This package includes several versions of Obliq:
  obliq:         Obliq interpreter
  obliq-3D:      Obliq interpreter with full 3D animation support
  obliq-anim:    Obliq interpreter with full animation support
  obliq-min:     Obliq interpreter with minimal runtime hooks
  obliq-std:     Obliq interpreter with the standard runtime hooks
  obliq-ui:      Obliq interpreter with ui support
  obliqsrv:      Obliq server
  obliqsrv-std:  Obliq server with the standard runtime hooks
  obliqsrv-ui:   Obliq server with ui support
  visobliq:      Prototype of an easy-to-use distributed programming
                 environment using Obliq

%package -n mentor
Summary:	A collection of algorithm animations
Group:		Development/Languages
Group(pl):	Programowanie/Jêzyki
Requires:	obliq = %{version}
Requires:	libpm3 = %{version}
Requires:	libpm3-extra = %{version}

%description -n mentor
Mentor encapsulates the Zeus animation library for Modula-3 into a single
application. Zeus itself is not very well documented, but a summary of the
animations which are part of the mentor application is available at:
http://www.research.digital.com/SRC/zeus/home.html

%prep
%setup -q
%patch -p1

%build
make -f Makefile.LINUXLIBC6 CFLAGS="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig -n libpm3
%post -p /sbin/ldconfig -n libpm3-extra
%post -p /sbin/ldconfig -n obliq

%postun -p /sbin/ldconfig -n libpm3
%postun -p /sbin/ldconfig -n libpm3-extra
%postun -p /sbin/ldconfig -n obliq

%files
/usr/bin/analyze_coverage
/usr/bin/m3build
/usr/bin/m3bundle
/usr/bin/m3coco
/usr/bin/m3ship
/usr/bin/m3tosgml
/usr/bin/sgmlconv
/usr/bin/sgmllinear
/usr/bin/sgmlnormalize
/usr/bin/sgmlstructure
/usr/bin/sgmltom3
/usr/man/man1/analyze_coverage.1
/usr/man/man1/m3bundle.1
/usr/lib/m3/pkg/coverage
/usr/lib/m3/pkg/libm3
/usr/lib/m3/pkg/m3back
/usr/lib/m3/pkg/m3build
/usr/lib/m3/pkg/m3bundle
/usr/lib/m3/pkg/m3coco
/usr/lib/m3/pkg/m3config
/usr/lib/m3/pkg/m3core
/usr/lib/m3/pkg/m3doc
/usr/lib/m3/pkg/m3driver
/usr/lib/m3/pkg/m3front
/usr/lib/m3/pkg/m3linker
/usr/lib/m3/pkg/m3middle
/usr/lib/m3/pkg/m3objfile
/usr/lib/m3/pkg/m3quake
/usr/lib/m3/pkg/m3ship
/usr/lib/m3/pkg/m3templates
/usr/lib/m3/pkg/m3tosgml
/usr/lib/m3/pkg/mtex
/usr/lib/m3/pkg/sgml
/usr/lib/m3/pkg/sgmlconv
/usr/lib/m3/pkg/sgmllinear
/usr/lib/m3/pkg/sgmlnormalize
/usr/lib/m3/pkg/sgmlstructure
/usr/lib/m3/pkg/sgmltom3
/usr/lib/m3/pkg/sgmltools
/usr/lib/m3/pkg/tempfiles
/usr/doc/pm3
m3build.1
m3coco.1
m3ship.1
m3tosgml.1
sgmlconv.1
sgmllinear.1
sgmlnormalize.1
sgmlstructure.1
sgmltom3.1

%files extra
WebCard.1
m3ide.1
m3tohtmlf.1
m3where.1

%files -n libpm3
/usr/lib/libTempFiles.so.1
/usr/lib/libm3.so.1
/usr/lib/libm3back.so.1
/usr/lib/libm3config.so.1
/usr/lib/libm3core.so.1
/usr/lib/libm3driver.so.1
/usr/lib/libm3front.so.1
/usr/lib/libm3link.so.1
/usr/lib/libm3middle.so.1
/usr/lib/libm3objfile.so.1
/usr/lib/libm3quake.so.1
/usr/lib/libm3templates.so.1
/usr/lib/libsgml.so.1
/usr/lib/m3/LINUXLIBC6/libTempFiles.so.1
/usr/lib/m3/LINUXLIBC6/libm3.so.1
/usr/lib/m3/LINUXLIBC6/libm3back.so.1
/usr/lib/m3/LINUXLIBC6/libm3config.so.1
/usr/lib/m3/LINUXLIBC6/libm3core.so.1
/usr/lib/m3/LINUXLIBC6/libm3driver.so.1
/usr/lib/m3/LINUXLIBC6/libm3front.so.1
/usr/lib/m3/LINUXLIBC6/libm3link.so.1
/usr/lib/m3/LINUXLIBC6/libm3middle.so.1
/usr/lib/m3/LINUXLIBC6/libm3objfile.so.1
/usr/lib/m3/LINUXLIBC6/libm3quake.so.1
/usr/lib/m3/LINUXLIBC6/libm3templates.so.1
/usr/lib/m3/LINUXLIBC6/libsgml.so.1
/usr/lib/m3/LINUXLIBC6/m3cgc1
/usr/lib/m3/LINUXLIBC6/report_coverage.o

%files -n m3gdb
/usr/bin/m3gdb
/usr/man/man1/m3gdb.1
/usr/lib/m3/pkg/m3gdb

%files -n obliq
/usr/bin/obliq
/usr/bin/obliq-3D
/usr/bin/obliq-anim
/usr/bin/obliq-min
/usr/bin/obliq-std
/usr/bin/obliq-ui
/usr/bin/obliqsrv
/usr/bin/obliqsrv-std
/usr/bin/obliqsrv-ui
/usr/bin/visobliq
/usr/bin/voquery
/usr/bin/vocgi
/usr/man/man1/obliq.1
/usr/man/man1/obliq-3D.1
/usr/man/man1/obliq-anim.1
/usr/man/man1/obliq-min.1
/usr/man/man1/obliq-std.1
/usr/man/man1/obliq-ui.1
/usr/man/man1/obliqsrv.1
/usr/man/man1/obliqsrv-std.1
/usr/man/man1/obliqsrv-ui.1
/usr/man/man1/visobliq.1
/usr/lib/libobliq.so.1
/usr/lib/libobliqlib3D.so.1
/usr/lib/libobliqlibanim.so.1
/usr/lib/libobliqlibm3.so.1
/usr/lib/libobliqlibui.so.1
/usr/lib/libobliqparse.so.1
/usr/lib/libobliqprint.so.1
/usr/lib/libobliqrt.so.1
/usr/lib/m3/LINUXLIBC6/libobliq.so.1
/usr/lib/m3/LINUXLIBC6/libobliqlib3D.so.1
/usr/lib/m3/LINUXLIBC6/libobliqlibanim.so.1
/usr/lib/m3/LINUXLIBC6/libobliqlibm3.so.1
/usr/lib/m3/LINUXLIBC6/libobliqlibui.so.1
/usr/lib/m3/LINUXLIBC6/libobliqparse.so.1
/usr/lib/m3/LINUXLIBC6/libobliqprint.so.1
/usr/lib/m3/LINUXLIBC6/libobliqrt.so.1
/usr/lib/m3/pkg/obliq
/usr/lib/m3/pkg/obliqbin3D
/usr/lib/m3/pkg/obliqbinanim
/usr/lib/m3/pkg/obliqbinmin
/usr/lib/m3/pkg/obliqbinstd
/usr/lib/m3/pkg/obliqbinui
/usr/lib/m3/pkg/obliqsrvstd
/usr/lib/m3/pkg/obliqsrvui
/usr/lib/m3/pkg/visualobliq
/usr/lib/m3/pkg/voquery
/usr/lib/m3/pkg/vocgi
/usr/lib/m3/pkg/vorun
/usr/lib/m3/pkg/m3obliq
/usr/lib/m3/pkg/obliqlib3D
/usr/lib/m3/pkg/obliqlibanim
/usr/lib/m3/pkg/obliqlibm3
/usr/lib/m3/pkg/obliqlibui
/usr/lib/m3/pkg/obliqparse
/usr/lib/m3/pkg/obliqprint
/usr/lib/m3/pkg/obliqrt
vocgi.1
voquery.1

%files -n mentor
/usr/bin/mentor
/usr/man/man1/mentor.1
/usr/lib/m3/pkg/mentor
