Summary:	The Polytechnique Montreal Modula-3 distribution
Summary(pl):	Dystrybucja Polytechnique Montreal Modula-3
Name:		pm3
Version:	1.1.15
Release:	1
License:	Open Source, mostly BSD like, some LGPL/GPL
Group:		Development/Languages/Modula3
Source0:	ftp://m3.polymtl.ca/pub/m3/targzip/%{name}-%{version}-src.tgz
# Source0-md5:	2688a6aae1155aa05026c99d67d0768e
Source1:	%{name}-LINUXLIBC6
Source2:	%{name}-COMMON
Source3:	ftp://m3.polymtl.ca/pub/m3/targzip/%{name}-%{version}-LINUXLIBC6-boot.tgz
# Source3-md5:	cc712010beb97ebdcdb87030fc84e93c
Patch0:		%{name}-readline.patch
Patch1:		%{name}-ncurses.patch
Patch2:		%{name}-m3gdb.patch
Patch3:		%{name}-glibc.patch
URL:		http://m3.polymtl.ca/m3/
# PM3 runs on several platforms but for Linux only on i386.
# Since RPM is mostly popular on Linux... let's stick to i386/Linux
ExclusiveArch:	%{ix86}
ExclusiveOS:	Linux
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Polytechnique Montreal Modula-3 distribution is based on the DEC
SRC Modula-3 programming environment.

Modula-3 is a systems programming language that descends from Mesa,
Modula-2, Cedar, and Modula-2+. It also resembles its cousins Object
Pascal, Oberon, and Euclid.

The goal of Modula-3 is to be as simple and safe as it can be while
meeting the needs of modern systems programmers. Instead of exploring
new features, they studied the features of the Modula family of
languages that have proven themselves in practice and tried to
simplify them into a harmonious language. They found that most of the
successful features were aimed at one of two main goals: greater
robustness, and a simpler, more systematic type system.

Modula-3 retains one of Modula-2's most successful features, the
provision for explicit interfaces between modules. It adds objects and
classes, exception handling, garbage collection, lightweight processes
(or threads), and the isolation of unsafe features.

A large number of platform independant libraries are available for
easily constructing distributed, graphical, multi-threaded
applications.

%description -l pl
Dystrybucja Polytechnique Montreal Modula-3 bazuje na ¶rodowisku
programistycznym DEC SRC Modula-3.

Modula-3 jest jêzykiem programowania wywodz±cym siê z jêzyków Mesa,
Modula-2, Cedar i Modula-2+. Kuzynami s± Object Pascal, Oberon i
Euclid.

Celem Moduli-3 jest byæ tak prostym i bezpiecznym, jak tylko mo¿liwe
zaspokajaj±c potrzeby wspó³czesnych programistów systemowych. Zamiast
zg³êbiaæ nowe cechy, studiowali cechy rodziny jêzyków Modula, które
sprawdzi³y siê w praktyce, i próbowali upro¶ciæ je w konsekwentny
jêzyk. Stwierdzili, ¿e wiêkszo¶æ cech zosta³a osi±gniêta w dwóch
g³ównych celach: wiêkszych mo¿liwo¶ciach i prostszym, bardziej
systematycznym systemie typów.

Modula-3 zachowuje najlepsze cechy Moduli-2, zapas interfejsów
pomiêdzy modu³ami. Dodaje obiekty i klasy, obs³ugê wyj±tków, garbage
collector, lekkie procesy (lub w±tki) i oddzielenie od niebezpiecznych
w³a¶ciwo¶ci.

S± dostêpne wiele bibliotek niezale¿nych od platformy dla ³atwego
tworzenia rozproszonych, graficznych, wielow±tkowych aplikacji.

%package mtex
Summary:	mtex is used to produce both troff man pages and HTML pages from the same source
Summary(pl):	mtex do produkcji stron man i HTML z tego samego ¼ród³a
Group:		Development/Languages/Modula3

%description mtex
mtex is used to produce both troff man pages and HTML pages from the
same source.

%description mtex -l pl
mtex s³u¿y do generowania podrêcznika man w formacie troff oraz HTML z
tego samego ¼ród³a.

%package m3doc
Summary:	m3doc produces both html and latex/postscript from the same source
Summary(pl):	m3doc do produkcji HTML i LaTeXa/postscripta z tego samego ¼ród³a
Group:		Development/Languages/Modula3

%description m3doc
m3doc produces both html and latex/postscript from the same source.

%description m3doc -l pl
m3doc s³u¿y do generowania dokumentów HTML i LaTeX/PostScript z tego
samego ¼ród³a.

%package m3coco
Summary:	Modula-3 LL(1) parser generator
Summary(pl):	Generator parserów LL(1) do Moduli-3
Group:		Development/Languages/Modula3

%description m3coco
Modula-3 LL(1) parser generator.

%description m3coco -l pl
Generator parserów LL(1) do Moduli-3.

%package tempfiles
Summary:	Library to build tempfiles
Summary(pl):	Biblioteka do budowania tempfile'i
Group:		Development/Languages/Modula3

%description tempfiles
Library to build tempfiles.

%description tempfiles -l pl
Biblioteka do budowania tempfile'i.

%package sgml
Summary:	SGML/XML parsing library
Summary(pl):	Biblioteka parsuj±ca SGML/XML
Group:		Development/Languages/Modula3

%description sgml
SGML/XML parsing library.

%description sgml -l pl
Biblioteka parsuj±ca SGML/XML.

%package m3tosgml
Summary:	Translate commented Modula-3 units into html files
Summary(pl):	Konwerter skomentowanych plików Modula-3 do HTML
Group:		Development/Languages/Modula3

%description m3tosgml
Translate commented Modula-3 units into html files.

%description m3tosgml -l pl
Narzêdzie do t³umaczenia skomentowanych plików w Moduli-3 na HTML.

%package sgmlconv
Summary:	Filter HTML files and convert HTML files to LaTeX
Summary(pl):	Filtr do plików HTML i konwerter do LaTeXa
Group:		Development/Languages/Modula3

%description sgmlconv
filter HTML files and convert HTML files to LaTeX.

%description sgmlconv -l pl
FIltr do plików HTML i konwerter HTML do LaTeXa.

%package sgmllinear
Summary:	Group several HTML files into a linear document
Summary(pl):	Konwerter grupuj±cy wiele plików HTML w jeden
Group:		Development/Languages/Modula3

%description sgmllinear
Group several HTML files into a linear document.

%description sgmllinear -l pl
Konwerter grupuj±cy wiele plików HTML w jeden ci±g³y dokument.

%package sgmltools
Summary:	SGML related tools
Summary(pl):	Narzêdzia zwi±zane z SGML
Group:		Development/Languages/Modula3

%description sgmltools
SGML related tools.

%description sgmltools -l pl
Narzêdzia zwi±zane z SGML.

%package m3textohtml
Summary:	Convert Modula-3 units from LaTeX markup to HTML markup
Summary(pl):	Konwerter plików Modula-3 z LaTeXa do HTML
Group:		Development/Languages/Modula3

%description m3textohtml
Convert Modula-3 units from LaTeX markup to HTML markup.

%description m3textohtml -l pl
Konwerter plików Modula-3 z LaTeXa do HTML.

%package sgmlnormalize
Summary:	Convert a SGML file to its canonical form
Summary(pl):	Konwerter SGML do postaci kanonicznej
Group:		Development/Languages/Modula3

%description sgmlnormalize
Convert a SGML file to its canonical form.

%description sgmlnormalize -l pl
Narzêdzie konwertujêce pliki SGML do postaci kanonicznej.

%package sgmlstructure
Summary:	Show the tree structure of a SGML file
Summary(pl):	Wy¶wietlanie struktury drzewiastej plików SGML
Group:		Development/Languages/Modula3

%description sgmlstructure
Show the tree structure of a SGML file.

%description sgmlstructure -l pl
Narzêdzie wy¶wietlaj±ce strukturê drzewiast± pliku SGML.

%package sgmltom3
Summary:	Convert back a Modula-3 unit from HTML to M3
Summary(pl):	Konwerter plików Modula-3 z HTML z powrotem do Moduli-3
Group:		Development/Languages/Modula3

%description sgmltom3
Convert back a Modula-3 unit from HTML to M3.

%description sgmltom3 -l pl
Konwerter plików Modula-3 z postaci HTML z powrotem do Moduli-3.

%package sil
Summary:	Sil is a simple drawing program that runs on Windows/NT
Summary(pl):	Sil - prosty program rysuj±cy pod Windows/NT
Group:		Development/Languages/Modula3

%description sil
Sil is a simple drawing program that runs on Windows/NT, Sample of
native Windows programming in Modula-3.

%description sil -l pl
Sil to prosty program do rysowania dzia³aj±cy pod Windows/NT -
przyk³ad natywnego programowania pod Windows w Moduli-3.

%package m3middle
Summary:	Modula-3 compiler's IL definition
Summary(pl):	Definicje IL dla kompilatora Modula-3
Group:		Development/Languages/Modula3

%description m3middle
Modula-3 compiler's IL definition.

%description m3middle -l pl
Definicje IL dla kompilatora Modula-3.

%package m3front
Summary:	Modula-3 compiler front-end
Summary(pl):	Frontend kompilatora Modula-3
Group:		Development/Languages/Modula3

%description m3front
Modula-3 compiler front-end.

%description m3front -l pl
Frontend kompilatora Modula-3.

%package m3linker
Summary:	Modula-3 prelinker
Summary(pl):	Prelinker Modula-3
Group:		Development/Languages/Modula3

%description m3linker
Modula-3 prelinker.

%description m3linker -l pl
Prelinker Modula-3.

%package m3objfile
Summary:	Modula-3 object file writers
Summary(pl):	Narzêdzia zapisuj±ce pliki obiektowe Modula-3
Group:		Development/Languages/Modula3

%description m3objfile
Modula-3 object file writers.

%description m3objfile -l pl
Narzêdzia zapisuj±ce pliki obiektowe Modula-3.

%package m3back
Summary:	Linux ELF and Windows/NT x86 back-ends
Summary(pl):	Backendy x86 Linux ELF i Windows/NT do Moduli-3
Group:		Development/Languages/Modula3

%description m3back
Linux ELF and Windows/NT x86 back-ends.

%description m3back -l pl
Backendy x86 Linux ELF i Windows/NT do Moduli-3.

%package m3driver
Summary:	Modula-3 compiler driver
Summary(pl):	Driver kompilatora Modula-3
Group:		Development/Languages/Modula3

%description m3driver
Modula-3 compiler driver.

%description m3driver -l pl
Driver kompilatora Modula-3.

%package m3staloneback
Summary:	Standalone back-end program like m3cc that uses m3back, used for testing
Summary(pl):	Samodzielny backend do testowania
Group:		Development/Languages/Modula3

%description m3staloneback
Standalone back-end program like m3cc that uses m3back, used for
testing.

%description m3staloneback -l pl
Samodzielny backend jak m3cc, który u¿ywa m3back, s³u¿±cy do
testowania.

%package m3loader
Summary:	An experimental dynamic loader for Windows/NT
Summary(pl):	Eksperymentalny loader dynamiczny dla Windows/NT
Group:		Development/Languages/Modula3

%description m3loader
An experimental dynamic loader for Windows/NT.

%description m3loader -l pl
Eksperymentalny loader dynamiczny dla Windows/NT.

%package m3quake
Summary:	The quake interpreter used by m3build
Summary(pl):	Interpreter quake u¿ywany przez m3build
Group:		Development/Languages/Modula3

%description m3quake
The quake interpreter used by m3build.

%description m3quake -l pl
Interpreter quake u¿ywany przez m3build.

%package m3templates
Summary:	Quake builtin functions for m3build
Summary(pl):	Wbudowane funkcje quake dla m3build
Group:		Development/Languages/Modula3

%description m3templates
Quake builtin functions for m3build.

%description m3templates -l pl
Wbudowane funkcje quake dla m3build.

%package m3-base
Summary:	The Modula-3 compiler
Summary(pl):	Kompilator Modula-3
Group:		Development/Languages/Modula3

%description m3-base
The Modula-3 compiler.

%description m3-base -l pl
Kompilator Modula-3.

%package m3bootstrap
Summary:	Cross compiles bootstrap packages for other platforms
Summary(pl):	Pakiety do kompilacji skro¶nej na inne platformy
Group:		Development/Languages/Modula3

%description m3bootstrap
Cross compiles bootstrap packages for other platforms.

%description m3bootstrap -l pl
Pakiety do kompilacji skro¶nej na inne platformy.

%package m3export
Summary:	Export and compiles a new release of PM3 from the CVS repository
Summary(pl):	Eksport i kompilacja nowej wersji PM3 z repozytorium CVS
Group:		Development/Languages/Modula3

%description m3export
Export and compiles a new release of PM3 from the CVS repository.

%description m3export -l pl
Narzêdzie eksportuj±ce i kompiluj±ce now± wersjê PM3 z repozytorium
CVS.

%package m3tests
Summary:	Tests for the Modula-3 compiler
Summary(pl):	Testy dla kompilatora Modula-3
Group:		Development/Languages/Modula3

%description m3tests
Tests for the Modula-3 compiler.

%description m3tests -l pl
Testy dla kompilatora Modula-3.

%package cg-burs
Summary:	An experimental Modula-3 back-end that uses BURS
Summary(pl):	Eksperymentalny backend Modula-3 u¿ywaj±cy BURS
Group:		Development/Languages/Modula3

%description cg-burs
An experimental Modula-3 back-end that uses BURS.

%description cg-burs -l pl
Eksperymentalny backend Modula-3 u¿ywaj±cy BURS.

%package coverage
Summary:	A line-based coverage analyzer/profiler
Summary(pl):	Liniowo zorientowany analizator/profiler
Group:		Development/Languages/Modula3

%description coverage
A line-based coverage analyzer/profiler.

%description coverage -l pl
Liniowo zorientowany analizator/profiler.

%package m3gdb
Summary:	Modula-3 aware debugger based on gdb
Summary(pl):	Debugger do Moduli-3 oparty o gdb
Group:		Development/Languages/Modula3

%description m3gdb
Modula-3 aware debugger based on gdb.

%description m3gdb -l pl
Debugger do Moduli-3 oparty o gdb.

%package pp
Summary:	Modula-3 pretty-printer
Summary(pl):	Wydruki dla Moduli-3
Group:		Development/Languages/Modula3

%description pp
Modula-3 pretty-printer.

%description pp -l pl
Wydruki dla Moduli-3.

%package m3totex
Summary:	Wraps Modula-3 source in enough TeX to make it printable
Summary(pl):	Filtr ¼róde³ Moduli-3 do TeXa w celu wydruku
Group:		Development/Languages/Modula3

%description m3totex
Wraps Modula-3 source in enough TeX to make it printable.

%description m3totex -l pl
Filtr opakowuj±cy ¼ród³a Moduli-3 w TeX, aby da³o siê je wydrukowaæ.

%package set
Summary:	A simple, generic Set interface
Summary(pl):	Prosty interfejs Set
Group:		Development/Languages/Modula3

%description set
A simple, generic Set interface.

%description set -l pl
Prosty interfejs Set.

%package digraph
Summary:	A directed graph type, generic over the types labeling nodes and edges
Summary(pl):	Typ skierowanego grafu, wspólny dla typów nazywaj±cych wêz³y i krawêdzie
Group:		Development/Languages/Modula3

%description digraph
A directed graph type, generic over the types labeling nodes and
edges.

%description digraph -l pl
Typ skierowanego grafu, wspólny dla typów nazywaj±cych wêz³y i
krawêdzie.

%package table-list
Summary:	An association-list-based, generic implementation of Table.T
Summary(pl):	Oparta o association-list, podstawowa implementacja Table.T
Group:		Development/Languages/Modula3

%description table-list
An association-list-based, generic implementation of Table.T.

%description table-list -l pl
Oparta o association-list, podstawowa implementacja Table.T.

%package realgeometry
Summary:	Geometry package (Point, Rect, Path, ...) with REAL-valued coordinates
Summary(pl):	Pakiet geometryczny (Point, Rect, Path...) ze wspó³rzêdnymi rzeczywistymi
Group:		Development/Languages/Modula3

%description realgeometry
Geometry package (Point, Rect, Path, ...) with REAL-valued
coordinates.

%description realgeometry -l pl
Pakiet geometryczny (Point, Rect, Path...) ze wspó³rzêdnymi
rzeczywistymi.

%package parseparams
Summary:	A library that helps parse command line arguments
Summary(pl):	Biblioteka pomocna przy parsowaniu linii poleceñ
Group:		Development/Languages/Modula3

%description parseparams
A library that helps parse command line arguments.

%description parseparams -l pl
Biblioteka pomagaj±ca przy parsowaniu argumentów linii poleceñ.

%package slisp
Summary:	A library containing a small Lisp interpreter
Summary(pl):	Biblioteka z ma³ym interpreterem Lispa
Group:		Development/Languages/Modula3

%description slisp
A library containing a small Lisp interpreter.

%description slisp -l pl
Biblioteka zawieraj±ca ma³y interpreter Lispa.

%package m3where
Summary:	Search for Modula-3 packages and files
Summary(pl):	Wyszukiwarka modu³ów i plików Modula-3
Group:		Development/Languages/Modula3

%description m3where
Search for Modula-3 packages and files.

%description m3where -l pl
Wyszukiwarka modu³ów i plików Modula-3.

%package tcp
Summary:	Implements a Modula-3 interface to TCP sockets
Summary(pl):	Interfejs Modula-3 do gniazdek TCP
Group:		Development/Languages/Modula3

%description tcp
Implements a Modula-3 interface to TCP sockets.

%description tcp -l pl
Implementacja interfejsu Modula-3 do gniazdek TCP.

%package web
Summary:	Library for retrieving documents from the World Wide Web using an http proxy server
Summary(pl):	Biblioteka do ¶ci±gania dokumentów z WWW przez proxy http
Group:		Development/Languages/Modula3

%description web
Library for retrieving documents from the World Wide Web using an http
proxy server.

%description web -l pl
Biblioteka do ¶ci±gania dokumentów z WWW przy u¿yciu proxy http.

%package m3tk
Summary:	Modula-3 abstract syntax tree (AST) toolkit
Summary(pl):	Toolkit Modula-3 do abstrakcyjnego drzewa sk³adni (AST)
Group:		Development/Languages/Modula3

%description m3tk
Modula-3 abstract syntax tree (AST) toolkit.

%description m3tk -l pl
Toolkit Modula-3 do abstrakcyjnego drzewa sk³adni (AST).

%package netobj
Summary:	The network objects runtime library
Summary(pl):	Biblioteka obiektów sieciowych
Group:		Development/Languages/Modula3

%description netobj
The network objects runtime library.

%description netobj -l pl
Biblioteka obiektów sieciowych.

%package stable
Summary:	A library providing log-based persistent objects
Summary(pl):	Biblioteka obiektów opartych o dziennik
Group:		Development/Languages/Modula3

%description stable
A library providing log-based persistent objects.

%description stable -l pl
Biblioteka dostarczaj±ca obiekty oparte o dziennik.

%package X11
Summary:	Modula-3 interface to the X library
Summary(pl):	Interfejs Modula-3 do biblioteki X
Group:		Development/Languages/Modula3

%description X11
Modula-3 interface to the X library.

%description X11 -l pl
Interfejs Modula-3 do biblioteki X.

%package PEX
Summary:	Modula-3 interface to the PEX 3D graphics library
Summary(pl):	Interfejs Modula-3 do biblioteki graficznej 3D PEX
Group:		Development/Languages/Modula3

%description PEX
Modula-3 interface to the PEX 3D graphics library.

%description PEX -l pl
Interfejs Modula-3 do biblioteki graficznej 3D PEX.

%package opengl
Summary:	Modula-3 interface to the OpenGL 3D graphics library
Summary(pl):	Interfejs Modula-3 do biblioteki graficznej 3D OpenGL
Group:		Development/Languages/Modula3

%description opengl
Modula-3 interface to the OpenGL 3D graphics library.

%description opengl -l pl
Interfejs Modula-3 do biblioteki graficznej 3D OpenGL.

%package motif
Summary:	Modula-3 interface to the X/Motif library
Summary(pl):	Interfejs Modula-3 do biblioteki X/Motif
Group:		Development/Languages/Modula3

%description motif
Modula-3 interface to the X/Motif library.

%description motif -l pl
Interfejs Modula-3 do biblioteki X/Motif.

%package tetris
Summary:	Modula-3 version of Tetris
Summary(pl):	Wersja Tetrisa w Moduli-3
Group:		Development/Languages/Modula3

%description tetris
Modula-3 version of Tetris.

%description tetris -l pl
Wersja Tetrisa napisana w Moduli-3.

%package columns
Summary:	Modula-3 version of the PC game, columns
Summary(pl):	Wersja gry columns w Moduli-3
Group:		Development/Languages/Modula3

%description columns
Modula-3 version of the PC game, columns.

%description columns -l pl
Wersja gry columns napisana w Moduli-3.

%package ui
Summary:	This library, ui, implements the Trestle window-system toolkit
Summary(pl):	Implementacja toolkitu okienkowego Trestle
Group:		Development/Languages/Modula3

%description ui
This library, ui, implements the Trestle window-system toolkit.

%description ui -l pl
Ta biblioteka to implementacja toolkitu okienkowego Trestle.

%package bicycle
Summary:	Library of playing card images
Summary(pl):	Biblioteka obrazków kart do gry
Group:		Development/Languages/Modula3

%description bicycle
Library of playing card images.

%description bicycle -l pl
Biblioteka obrazków kart do gry.

%package solitaire
Summary:	Modula-3 version of SeaHaven towers
Summary(pl):	Wersja pasjansa SeaHaven towers w Moduli-3
Group:		Development/Languages/Modula3

%description solitaire
Modula-3 version of SeaHaven towers.

%description solitaire -l pl
Wersja pasjansa SeaHaven towers napisana w Moduli-3.

%package badbricks
Summary:	Modula-3 game similar to minesweeper, inspired by the crumbling facade of SRC's building
Summary(pl):	Gra podobna do sapera w Moduli-3
Group:		Development/Languages/Modula3

%description badbricks
Modula-3 game similar to minesweeper, inspired by the crumbling facade
of SRC's building.

%description badbricks -l pl
Gra napisana w Moduli-3 podobna do sapera (Minesweepera).

%package m3scan
Summary:	Simple Modula-3 lexical token scanner
Summary(pl):	Prosty skaner tokenów leksykalnych do Moduli-3
Group:		Development/Languages/Modula3

%description m3scan
Simple Modula-3 lexical token scanner.

%description m3scan -l pl
Prosty skaner tokenów leksykalnych do Moduli-3.

%package m3tohtml
Summary:	Convert batches of Modula-3 source to interconnected HTML
Summary(pl):	Konwerter paczek ¼róde³ w Moduli-3 na powi±zany HTML
Group:		Development/Languages/Modula3

%description m3tohtml
Convert batches of Modula-3 source to interconnected HTML.

%description m3tohtml -l pl
Konwerter paczek ¼róde³ w Moduli-3 na HTML z powi±zaniami.

%package m3markup
Summary:	Parse Modula-3 source code and insert HTML markup
Summary(pl):	Parser ¼róde³ w Moduli-3 wstawiaj±cy tagi HTML
Group:		Development/Languages/Modula3

%description m3markup
Parse Modula-3 source code and insert HTML markup.

%description m3markup -l pl
Parser ¼róde³ w Moduli-3 wstawiaj±cy tagi HTML.

%package m3tohtmlf
Summary:	Convert one Modula-3 source to an HTML file
Summary(pl):	Konwerter pojedynczego ¼ród³a w Moduli-3 na plik HTML
Group:		Development/Languages/Modula3

%description m3tohtmlf
Convert one Modula-3 source to an HTML file.

%description m3tohtmlf -l pl
Konwerter pojedynczego ¼ród³a w Moduli-3 na plik HTML.

%package tcpextras
Summary:	Additions to the tcp library
Summary(pl):	Dodatki do biblioteki tcp
Group:		Development/Languages/Modula3

%description tcpextras
Additions to the tcp library.

%description tcpextras -l pl
Dodatki do biblioteki tcp.

%package m3browser
Summary:	HTTP server that provides WWW browsing of the installed Modula-3 system
Summary(pl):	Serwer HTTP pozwalaj±cy na przegl±danie systemu Modula-3 przez WWW
Group:		Development/Languages/Modula3

%description m3browser
HTTP server that provides WWW browsing of the installed Modula-3
system.

%description m3browser -l pl
Serwer HTTP pozwalaj±cy na przegl±danie przez WWW zainstalowanego
systemu Modula-3.

%package tcl
Summary:	Thin Modula-3 veneer on the TCL library (version 6.2)
Summary(pl):	Wrapper Modula-3 do biblioteki TCL (w wersji 6.2)
Group:		Development/Languages/Modula3

%description tcl
Thin Modula-3 veneer on the TCL library (version 6.2).

%description tcl -l pl
Wrapper Modula-3 do biblioteki TCL (w wersji 6.2).

%package dps
Summary:	Thin Modula-3 veneer on the display Postscript extensions to X
Summary(pl):	Wrapper Modula-3 do rozszerzeñ X wy¶wietlaj±cych Postscript
Group:		Development/Languages/Modula3

%description dps
Thin Modula-3 veneer on the display Postscript extensions to X.

%description dps -l pl
Wrapper Modula-3 do rozszerzeñ X wy¶wietlaj±cych Postscript.

%package dpsslides
Summary:	Program to display postscript slides in X
Summary(pl):	Program wy¶wietlaj±cy slajdy w Postscripcie pod X
Group:		Development/Languages/Modula3

%description dpsslides
Program to display postscript slides in X.

%description dpsslides -l pl
Program wy¶wietlaj±cy slajdy w Postscripcie pod X.

%package vbtkit
Summary:	Large collection of useful window widgets
Summary(pl):	Du¿y zbiór u¿ytecznych widgetów okienkowych
Group:		Development/Languages/Modula3

%description vbtkit
Large collection of useful window widgets.

%description vbtkit -l pl
Du¿y zbiór u¿ytecznych widgetów okienkowych.

%package fours
Summary:	Modula-3 variants of the PC game, tetris
Summary(pl):	Warianty gry Tetris w Moduli-3
Group:		Development/Languages/Modula3

%description fours
Modula-3 variants of the PC game, tetris.

%description fours -l pl
Warianty gry Tetris w Moduli-3.

%package showheap
Summary:	Graphically display in real-time the state of each heap page
Summary(pl):	Graficzne wy¶wietlanie stanu stron sterty
Group:		Development/Languages/Modula3

%description showheap
Graphically display in real-time the state of each heap page.

%description showheap -l pl
Graficzne wy¶wietlanie stanu stron sterty.

%package recordheap
Summary:	Program to capture a showheap trace
Summary(pl):	Program do zachowywania wyników showheap
Group:		Development/Languages/Modula3

%description recordheap
Program to capture a showheap trace.

%description recordheap -l pl
Program do zachowywania wyników showheap.

%package replayheap
Summary:	Graphically display the log captured by recordheap
Summary(pl):	Graficzne wy¶wietlanie loga zachowanego przez recordheap
Group:		Development/Languages/Modula3

%description replayheap
Graphically display the log captured by recordheap.

%description replayheap -l pl
Graficzne wy¶wietlanie loga zachowanego przez recordheap.

%package shownew
Summary:	Graphically display in real-time per-type allocations
Summary(pl):	Graficzne wy¶wietlanie alokacji w czasie rzeczywistym
Group:		Development/Languages/Modula3

%description shownew
Graphically display in real-time per-type allocations.

%description shownew -l pl
Graficzne wy¶wietlanie alokacji w zale¿no¶ci od typu w czasie
rzeczywistym.

%package showthread
Summary:	Graphically display in real-time the state of each thread
Summary(pl):	Graficzne wy¶wietlanie stanu w±tków w czasie rzeczywistym
Group:		Development/Languages/Modula3

%description showthread
Graphically display in real-time the state of each thread.

%description showthread -l pl
Graficzne wy¶wietlanie stanu w±tków w czasie rzeczywistym.

%package images
Summary:	Support for displaying bitmap images
Summary(pl):	Wsparcie dla wy¶wietlania obrazków
Group:		Development/Languages/Modula3

%description images
Support for displaying bitmap images.

%description images -l pl
Wsparcie dla wy¶wietlania obrazków.

%package jvideo
Summary:	Low-level interface to the J-video hardware, needed by videovbt
Summary(pl):	Niskopoziomowy interfejs do urz±dzeñ J-video, potrzebny do videovbt
Group:		Development/Languages/Modula3

%description jvideo
Low-level interface to the J-video hardware, needed by videovbt.

%description jvideo -l pl
Niskopoziomowy interfejs do urz±dzeñ J-video, potrzebny do videovbt.

%package videovbt
Summary:	Window widget that displays live video images
Summary(pl):	Widget okienkowy wy¶wietlaj±cy filmy
Group:		Development/Languages/Modula3

%description videovbt
Window widget that displays live video images.

%description videovbt -l pl
Widget okienkowy wy¶wietlaj±cy filmy.

%package formsvbtpixmaps
Summary:	Bitmaps, cursors and stuff used by formsvbt
Summary(pl):	Bitmapy, kursory i inne rzeczy u¿ywane przez formsvbt
Group:		Development/Languages/Modula3

%description formsvbtpixmaps
Bitmaps, cursors and stuff used by formsvbt.

%description formsvbtpixmaps -l pl
Bitmapy, kursory i inne rzeczy u¿ywane przez formsvbt.

%package formsvbt
Summary:	High-level language based on S-expressions that makes it easy to assemble VBTs (windows) using the TeX metaphors of boxes and glue
Summary(pl):	Wysokopoziomowy jêzyk bazuj±cy na S-wyra¿eniach u³atwiaj±cy sk³adanie VBT podobnie do TeXa
Group:		Development/Languages/Modula3

%description formsvbt
High-level language based on S-expressions that makes it easy to
assemble VBTs (windows) using the TeX metaphors of boxes and glue.

%description formsvbt -l pl
Wysokopoziomowy jêzyk bazuj±cy na S-wyra¿eniach pozwalaj±cy ³atwo
sk³adaæ VBT (okienka) u¿ywaj±c TeXowych okre¶leñ "pude³ek i kleju".

%package formsedit
Summary:	A 1-1/2 view GUI editor for FormsVBT expressions
Summary(pl):	Edytor graficzny wyra¿eñ FormsVBT
Group:		Development/Languages/Modula3

%description formsedit
A 1-1/2 view GUI editor for FormsVBT expressions.

%description formsedit -l pl
Edytor graficzny wyra¿eñ FormsVBT.

%package m3ide
Summary:	Simple integrated development environment based on emacs
Summary(pl):	Zintegorowane ¶rodowisko programistyczne bazuj±ce na emacsie
Group:		Development/Languages/Modula3

%description m3ide
Simple integrated development environment based on emacs.

%description m3ide -l pl
Proste zintegrowane ¶rodowisko programistyczne bazuj±ce na emacsie.

%package fisheye
Summary:	A demo of fisheye views for graph browsing
Summary(pl):	Demo widoków do przegl±dania grafów
Group:		Development/Languages/Modula3

%description fisheye
A demo of fisheye views for graph browsing.

%description fisheye -l pl
Demo widoków do przegl±dania grafów.

%package calculator
Summary:	A 10-key calculator using FormsVBT
Summary(pl):	10-klawiszowy kalkulator u¿ywaj±cy FormsVBT
Group:		Development/Languages/Modula3

%description calculator
A 10-key calculator using FormsVBT.

%description calculator -l pl
10-klawiszowy kalkulator u¿ywaj±cy FormsVBT.

%package cube
Summary:	A rotating cube
Summary(pl):	Obracaj±ca siê kostka
Group:		Development/Languages/Modula3

%description cube
A rotating cube.

%description cube -l pl
Obracaj±ca siê kostka.

%package board
Summary:	A network object graphical board
Summary(pl):	Obiekt sieciowy tablicy graficznej
Group:		Development/Languages/Modula3

%description board
A network object graphical board.

%description board -l pl
Okiekt sieciowy tablicy graficznej.

%package codeview
Summary:	Support for animated views of source code
Summary(pl):	Wsparcie dla animowanego podgl±du kodu ¼ród³owego
Group:		Development/Languages/Modula3

%description codeview
Support for animated views of source code.

%description codeview -l pl
Wsparcie dla animowanego kodu ¼ród³owego.

%package rehearsecode
Summary:	Program to manually test drive source code animations
Summary(pl):	Program do testowania animacji kodu ¼ród³owego
Group:		Development/Languages/Modula3

%description rehearsecode
Program to manually test drive source code animations.

%description rehearsecode -l pl
Program do rêcznego testowania animacji kodu ¼ród³owego.

%package mg
Summary:	Low-level animation support
Summary(pl):	Niskopoziomowe wsparcie dla animacji
Group:		Development/Languages/Modula3

%description mg
Low-level animation support.

%description mg -l pl
Niskopoziomowe wsparcie dla animacji.

%package mgkit
Summary:	Collection of easier-to-use animation widgets
Summary(pl):	Zestaw widgetów do animacji
Group:		Development/Languages/Modula3

%description mgkit
Collection of easier-to-use animation widgets.

%description mgkit -l pl
Zestaw ³atwych w u¿yciu widgetów do animacji.

%package anim3D
Summary:	Collection of 3D animation widgets
Summary(pl):	Zestaw widgetów do animacji 3D
Group:		Development/Languages/Modula3

%description anim3D
Collection of 3D animation widgets.

%description anim3D -l pl
Zestaw widgetów do animacji 3D.

%package synloc
Summary:	Library for syntaxic analysis
Summary(pl):	BIblioteka analizy sk³adniowej
Group:		Development/Languages/Modula3

%description synloc
Library for syntaxic analysis.

%description synloc -l pl
Biblioteka analizy sk³adniowej.

%package synex
Summary:	Extensions to synloc
Summary(pl):	Rozszerzenia do synloc
Group:		Development/Languages/Modula3

%description synex
Extensions to synloc.

%description synex -l pl
Rozszerzenia do synloc.

%package metasyn
Summary:	Meta syntax for synex
Summary(pl):	Metask³adnia do synex
Group:		Development/Languages/Modula3

%description metasyn
Meta syntax for synex.

%description metasyn -l pl
Metask³adnia dla synex.

%package obliq
Summary:	The Obliq interpreter
Summary(pl):	Interpreter Obliq
Group:		Development/Languages/Modula3

%description obliq
The Obliq interpreter.

%description obliq -l pl
Interpreter Obliq.

%package sgmlobliq
Summary:	Integrate the sgml library to Obliq
Summary(pl):	Zintegrowana biblioteka SGML do Obliq
Group:		Development/Languages/Modula3

%description sgmlobliq
Integrate the sgml library to Obliq.

%description sgmlobliq -l pl
Zintegrowana biblioteka SGML do Obliq.

%package m3zume
Summary:	The interesting event preprocessor needed by zeus
Summary(pl):	Preprocesor zdarzeñ potrzebny do zeusa
Group:		Development/Languages/Modula3

%description m3zume
The interesting event preprocessor needed by zeus.

%description m3zume -l pl
Preprocesor zdarzeñ potrzebny do zeusa.

%package zeus
Summary:	The algorithm animation toolkit
Summary(pl):	Toolkit do animacji algorytmicznych
Group:		Development/Languages/Modula3

%description zeus
The algorithm animation toolkit.

%description zeus -l pl
Toolkit do animacji algorytmicznych.

%package mentor
Summary:	A collection of algoritm animations
Summary(pl):	Zestaw animacji algorytmicznych
Group:		Development/Languages/Modula3

%description mentor
A collection of algoritm animations.

%description mentor -l pl
Zestaw animacji algorytmicznych.

%package smalldb
Summary:	In-memory database library, used by the package tools
Summary(pl):	Biblioteka bazy danych trzymanej w pamiêci
Group:		Development/Languages/Modula3

%description smalldb
In-memory database library, used by the package tools.

%description smalldb -l pl
Biblioteka bazy danych przechowywanej w pamiêci, u¿ywanej przez
narzêdzia pakietowe.

%package pkgtool
Summary:	Client program(s) to access the package tools
Summary(pl):	Program(y) klienckie dostêpu do narzêdzi pakietowych
Group:		Development/Languages/Modula3

%description pkgtool
Client program(s) to access the package tools.

%description pkgtool -l pl
Program(y) klienckie dostêpu do narzêdzi pakietowych.

%package visualobliq
Summary:	Prototype of an easy-to-use distributed programming environment
Summary(pl):	Prototyp ¶rodowiska do programowania rozproszonego
Group:		Development/Languages/Modula3

%description visualobliq
Prototype of an easy-to-use distributed programming environment.

%description visualobliq -l pl
Prototyp ³atwego w u¿yciu ¶rodowiska do programowania rozproszonego.

%package voquery
Summary:	A simple query program used by vorun
Summary(pl):	Prosty program zapytañ u¿ywany przez vorun
Group:		Development/Languages/Modula3

%description voquery
A simple query program used by vorun.

%description voquery -l pl
Prosty program zapytañ u¿ywany przez vorun.

%package vorun
Summary:	A safe visual obliq interpreter suitable for embedding in the WWW
Summary(pl):	Bezpieczny wizualny interpreter Obliq do zagnie¿d¿ania w WWW
Group:		Development/Languages/Modula3

%description vorun
A safe visual obliq interpreter suitable for embedding in the WWW.

%description vorun -l pl
Bezpieczny wizualny interpreter Obliq nadaj±cy siê do zagnie¿d¿ania w
WWW.

%package vocgi
Summary:	An HTML/cgi gateway, required to embed Visual Obliq code in the WWW
Summary(pl):	Bramka HTML/cgi, potrzebna do zagnie¿d¿ania Visual Obliq w WWW
Group:		Development/Languages/Modula3

%description vocgi
An HTML/cgi gateway, required to embed Visual Obliq code in the WWW.

%description vocgi -l pl
Bramka HTML/cgi potrzebna do zagnie¿d¿ania kodu Visual Obliq w WWW.

%package llscan
Summary:	A little mh program used by Postcard
Summary(pl):	Ma³y program mh u¿ywany przez Postcard
Group:		Development/Languages/Modula3

%description llscan
A little mh program used by Postcard.

%description llscan -l pl
Ma³y program mh u¿ywany przez Postcard.

%package postcard
Summary:	An integrated mail/news reader
Summary(pl):	Zintegrowany czytnik poczty i newsów
Group:		Development/Languages/Modula3

%description postcard
An integrated mail/news reader.

%description postcard -l pl
Zintegrowany czytnik poczty i newsów.

%package gnuemacs
Summary:	A library of useful E-lisp code for Modula-3-mode in gnuemacs, also a program to build Modula-3 tags
Summary(pl):	Biblioteka kodu E-lisp do trybu Modula-3 w GNU emacsie
Group:		Development/Languages/Modula3

%description gnuemacs
A library of useful E-lisp code for Modual-3-mode in gnuemacs, also a
program to build Modula-3 tags.

%description gnuemacs -l pl
Biblioteka przydatnego kodu E-lisp do trubu Modula-3 w GNU emacsie, a
tak¿e program do budowania tagów Modula-3.

%package webvbt
Summary:	A library for displaying HTML pages inside a VBT
Summary(pl):	Biblioteka do wy¶wietlania stron HTML w VBT
Group:		Development/Languages/Modula3

%description webvbt
A library for displaying HTML pages inside a VBT.

%description webvbt -l pl
Biblioteka do wy¶wietlania stron HTML w VBT.

%package webscape
Summary:	A web browser with support for interactive content
Summary(pl):	Przegl±darka WWW ze wsparciem dla zawarto¶ci interaktywnej
Group:		Development/Languages/Modula3

%description webscape
A web browser with support for interactive content.

%description webscape -l pl
Przegl±darka WWW ze wsparciem dla zawarto¶ci interaktywnej.

%package deckscape
Summary:	A web browser that uses a new metaphor: decks of web pages
Summary(pl):	Przegl±darka WWW u¿ywaj±ca nowego stylu: pokrycia stron WWW
Group:		Development/Languages/Modula3

%description deckscape
A web browser that uses a new metaphor: decks of web pages.

%description deckscape -l pl
Przegl±darka WWW u¿ywaj±ca nowego stylu: pokrycia stron WWW.

%package webcard
Summary:	An integrated mail/news/web client
Summary(pl):	Zintegrowany klient poczty, newsów i WWW
Group:		Development/Languages/Modula3

%description webcard
An integrated mail/news/web client.

%description webcard -l pl
Zintegrowany klient poczty, newsów i WWW.

%package ocr
Summary:	Interface to optical character recognition library (DECstation only)
Summary(pl):	Interfejs do biblioteki OCR (tylko DECstation)
Group:		Development/Languages/Modula3

%description ocr
Interface to optical character recognition library (DECstation only).

%description ocr -l pl
Interfejs do biblioteki OCR (optycznego rozpoznawania znaków) (tylko
na DECstation).

%package lectern
Summary:	The virtual paper document viewer
Summary(pl):	Przegl±darka wirtualnych dokumentów
Group:		Development/Languages/Modula3

%description lectern
The virtual paper document viewer.

%description lectern -l pl
Przegl±darka wirtualnych dokumentów.

%package http
Summary:	Library for hypertext transfer protocol (HTTP)
Summary(pl):	Biblioteka obs³ugi protoko³u HTTP
Group:		Development/Languages/Modula3

%description http
Library for hypertext transfer protocol (HTTP).

%description http -l pl
Biblioteka obs³ugi protoko³u HTTP.

%package webcat
Summary:	Program that takes a URL and prints out the web document
Summary(pl):	Program przyjmuj±cy URL i drukuj±cy wskazywany dokument
Group:		Development/Languages/Modula3

%description webcat
Program that takes a URL and prints out the web document.

%description webcat -l pl
Program przyjmuj±cy URL i drukuj±cy wskazywany przez niego dokument.

%package m3intro
Summary:	Introduction and documentation for Polytechnique Montreal Modula-3
Summary(pl):	Wprowadzenie i dokumentacja do Polytechnique Montreal Modula-3
Group:		Development/Languages/Modula3

%description m3intro
Introduction and documentation for Polytechnique Montreal Modula-3.

%description m3intro -l pl
Wprowadzenie i dokumentacja do Polytechnique Montreal Modula-3.

%prep
%setup -q -b3
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
install %{SOURCE1} m3config/src/LINUXLIBC6
install %{SOURCE2} m3config/src/COMMON
rm -rf $RPM_BUILD_ROOT

%build
%{__make} \
	M3OPTIONS="-DLIST_FILES -DSETROOT=%{_prefix} -DEXPORTPATH=$RPM_BUILD_ROOT"

%install
rm -rf $RPM_BUILD_ROOT
%{__make} nothing

cd files
for i in * ; do
	mv -f $i $i.bak
	sed -e 's/\(man\/man[0-9]\/.*\.[0-9]\)/\1\*/' $i.bak > $i
done

%clean
rm -rf $RPM_BUILD_ROOT

%files rehearsecode -f files/rehearsecode
%defattr(644,root,root,755)
%docdir %{_libdir}/m3/www

%files webscape -f files/webscape
%defattr(644,root,root,755)
%docdir %{_libdir}/m3/www

%files m3tosgml -f files/m3tosgml
%defattr(644,root,root,755)
%docdir %{_libdir}/m3/www

%files dps -f files/dps
%defattr(644,root,root,755)
%docdir %{_libdir}/m3/www

%files m3ide -f files/m3ide
%defattr(644,root,root,755)
%docdir %{_libdir}/m3/www

%files m3staloneback -f files/m3staloneback
%defattr(644,root,root,755)
%docdir %{_libdir}/m3/www

%files metasyn -f files/metasyn
%defattr(644,root,root,755)
%docdir %{_libdir}/m3/www

%files sgmlstructure -f files/sgmlstructure
%defattr(644,root,root,755)
%docdir %{_libdir}/m3/www

%files m3coco -f files/m3coco
%defattr(644,root,root,755)
%docdir %{_libdir}/m3/www

%files tcp -f files/tcp
%defattr(644,root,root,755)
%docdir %{_libdir}/m3/www

%files formsvbtpixmaps -f files/formsvbtpixmaps
%defattr(644,root,root,755)
%docdir %{_libdir}/m3/www

%files m3linker -f files/m3linker
%defattr(644,root,root,755)
%docdir %{_libdir}/m3/www

%files tetris -f files/tetris
%defattr(644,root,root,755)
%docdir %{_libdir}/m3/www

%files pkgtool -f files/pkgtool
%defattr(644,root,root,755)
%docdir %{_libdir}/m3/www

%files m3gdb -f files/m3gdb
%defattr(644,root,root,755)
%docdir %{_libdir}/m3/www

%files realgeometry -f files/realgeometry
%defattr(644,root,root,755)
%docdir %{_libdir}/m3/www

%files showthread -f files/showthread
%defattr(644,root,root,755)
%docdir %{_libdir}/m3/www

%files codeview -f files/codeview
%defattr(644,root,root,755)
%docdir %{_libdir}/m3/www

%files tcl -f files/tcl
%defattr(644,root,root,755)
%docdir %{_libdir}/m3/www

%files ui -f files/ui
%defattr(644,root,root,755)
%docdir %{_libdir}/m3/www

%files mtex -f files/mtex
%defattr(644,root,root,755)
%docdir %{_libdir}/m3/www

%files lectern -f files/lectern
%defattr(644,root,root,755)
%docdir %{_libdir}/m3/www

%files m3totex -f files/m3totex
%defattr(644,root,root,755)
%docdir %{_libdir}/m3/www

%files showheap -f files/showheap
%defattr(644,root,root,755)
%docdir %{_libdir}/m3/www

%files llscan -f files/llscan
%defattr(644,root,root,755)
%docdir %{_libdir}/m3/www

%files m3markup -f files/m3markup
%defattr(644,root,root,755)
%docdir %{_libdir}/m3/www

%files motif -f files/motif
%defattr(644,root,root,755)
%docdir %{_libdir}/m3/www

%files mg -f files/mg
%defattr(644,root,root,755)
%docdir %{_libdir}/m3/www

%files deckscape -f files/deckscape
%defattr(644,root,root,755)
%docdir %{_libdir}/m3/www

%files sgmlconv -f files/sgmlconv
%defattr(644,root,root,755)
%docdir %{_libdir}/m3/www

%files fisheye -f files/fisheye
%defattr(644,root,root,755)
%docdir %{_libdir}/m3/www

%files visualobliq -f files/visualobliq
%defattr(644,root,root,755)
%docdir %{_libdir}/m3/www

%files sgmltom3 -f files/sgmltom3
%defattr(644,root,root,755)
%docdir %{_libdir}/m3/www

%files m3zume -f files/m3zume
%defattr(644,root,root,755)
%docdir %{_libdir}/m3/www

%files m3export -f files/m3export
%defattr(644,root,root,755)
%docdir %{_libdir}/m3/www

%files m3objfile -f files/m3objfile
%defattr(644,root,root,755)
%docdir %{_libdir}/m3/www

%files m3-base -f files/m3-base
%defattr(644,root,root,755)
%docdir %{_libdir}/m3/www

%files http -f files/http
%defattr(644,root,root,755)
%docdir %{_libdir}/m3/www

%files parseparams -f files/parseparams
%defattr(644,root,root,755)
%docdir %{_libdir}/m3/www

%files images -f files/images
%defattr(644,root,root,755)
%docdir %{_libdir}/m3/www

%files opengl -f files/opengl
%defattr(644,root,root,755)
%docdir %{_libdir}/m3/www

%files X11 -f files/X11
%defattr(644,root,root,755)
%docdir %{_libdir}/m3/www

%files m3tk -f files/m3tk
%defattr(644,root,root,755)
%docdir %{_libdir}/m3/www

%files bicycle -f files/bicycle
%defattr(644,root,root,755)
%docdir %{_libdir}/m3/www

%files set -f files/set
%defattr(644,root,root,755)
%docdir %{_libdir}/m3/www

%files recordheap -f files/recordheap
%defattr(644,root,root,755)
%docdir %{_libdir}/m3/www

%files sgmlobliq -f files/sgmlobliq
%defattr(644,root,root,755)
%docdir %{_libdir}/m3/www

%files m3tohtmlf -f files/m3tohtmlf
%defattr(644,root,root,755)
%docdir %{_libdir}/m3/www

%files mgkit -f files/mgkit
%defattr(644,root,root,755)
%docdir %{_libdir}/m3/www

%files webcard -f files/webcard
%defattr(644,root,root,755)
%docdir %{_libdir}/m3/www

%files sgmllinear -f files/sgmllinear
%defattr(644,root,root,755)
%docdir %{_libdir}/m3/www

%files dpsslides -f files/dpsslides
%defattr(644,root,root,755)
%docdir %{_libdir}/m3/www

%files calculator -f files/calculator
%defattr(644,root,root,755)
%docdir %{_libdir}/m3/www

%files voquery -f files/voquery
%defattr(644,root,root,755)
%docdir %{_libdir}/m3/www

%files obliq -f files/obliq
%defattr(644,root,root,755)
%docdir %{_libdir}/m3/www

%files sil -f files/sil
%defattr(644,root,root,755)
%docdir %{_libdir}/m3/www

%files PEX -f files/PEX
%defattr(644,root,root,755)
%docdir %{_libdir}/m3/www

%files zeus -f files/zeus
%defattr(644,root,root,755)
%docdir %{_libdir}/m3/www

%files m3back -f files/m3back
%defattr(644,root,root,755)
%docdir %{_libdir}/m3/www

%files coverage -f files/coverage
%defattr(644,root,root,755)
%docdir %{_libdir}/m3/www

%files stable -f files/stable
%defattr(644,root,root,755)
%docdir %{_libdir}/m3/www

%files m3templates -f files/m3templates
%defattr(644,root,root,755)
%docdir %{_libdir}/m3/www

%files slisp -f files/slisp
%defattr(644,root,root,755)
%docdir %{_libdir}/m3/www

%files webcat -f files/webcat
%defattr(644,root,root,755)
%docdir %{_libdir}/m3/www

%files jvideo -f files/jvideo
%defattr(644,root,root,755)
%docdir %{_libdir}/m3/www

%files m3middle -f files/m3middle
%defattr(644,root,root,755)
%docdir %{_libdir}/m3/www

%files cg-burs -f files/cg-burs
%defattr(644,root,root,755)
%docdir %{_libdir}/m3/www

%files netobj -f files/netobj
%defattr(644,root,root,755)
%docdir %{_libdir}/m3/www

%files solitaire -f files/solitaire
%defattr(644,root,root,755)
%docdir %{_libdir}/m3/www

%files m3doc -f files/m3doc
%defattr(644,root,root,755)
%docdir %{_libdir}/m3/www

%files digraph -f files/digraph
%defattr(644,root,root,755)
%docdir %{_libdir}/m3/www

%files replayheap -f files/replayheap
%defattr(644,root,root,755)
%docdir %{_libdir}/m3/www

%files postcard -f files/postcard
%defattr(644,root,root,755)
%docdir %{_libdir}/m3/www

%files m3bootstrap -f files/m3bootstrap
%defattr(644,root,root,755)
%docdir %{_libdir}/m3/www

%files tcpextras -f files/tcpextras
%defattr(644,root,root,755)
%docdir %{_libdir}/m3/www

%files anim3D -f files/anim3D
%defattr(644,root,root,755)
%docdir %{_libdir}/m3/www

%files ocr -f files/ocr
%defattr(644,root,root,755)
%docdir %{_libdir}/m3/www

%files vbtkit -f files/vbtkit
%defattr(644,root,root,755)
%docdir %{_libdir}/m3/www

%files sgmltools -f files/sgmltools
%defattr(644,root,root,755)
%docdir %{_libdir}/m3/www

%files cube -f files/cube
%defattr(644,root,root,755)
%docdir %{_libdir}/m3/www

%files m3quake -f files/m3quake
%defattr(644,root,root,755)
%docdir %{_libdir}/m3/www

%files vorun -f files/vorun
%defattr(644,root,root,755)
%docdir %{_libdir}/m3/www

%files m3scan -f files/m3scan
%defattr(644,root,root,755)
%docdir %{_libdir}/m3/www

%files mentor -f files/mentor
%defattr(644,root,root,755)
%docdir %{_libdir}/m3/www

%files webvbt -f files/webvbt
%defattr(644,root,root,755)
%docdir %{_libdir}/m3/www

%files m3tests -f files/m3tests
%defattr(644,root,root,755)
%docdir %{_libdir}/m3/www

%files sgml -f files/sgml
%defattr(644,root,root,755)
%docdir %{_libdir}/m3/www

%files m3driver -f files/m3driver
%defattr(644,root,root,755)
%docdir %{_libdir}/m3/www

%files formsedit -f files/formsedit
%defattr(644,root,root,755)
%docdir %{_libdir}/m3/www

%files synex -f files/synex
%defattr(644,root,root,755)
%docdir %{_libdir}/m3/www

%files sgmlnormalize -f files/sgmlnormalize
%defattr(644,root,root,755)
%docdir %{_libdir}/m3/www

%files m3intro -f files/m3intro
%defattr(644,root,root,755)
%docdir %{_libdir}/m3/www

%files m3where -f files/m3where
%defattr(644,root,root,755)
%docdir %{_libdir}/m3/www

%files videovbt -f files/videovbt
%defattr(644,root,root,755)
%docdir %{_libdir}/m3/www

%files m3front -f files/m3front
%defattr(644,root,root,755)
%docdir %{_libdir}/m3/www

%files m3loader -f files/m3loader
%defattr(644,root,root,755)
%docdir %{_libdir}/m3/www

%files badbricks -f files/badbricks
%defattr(644,root,root,755)
%docdir %{_libdir}/m3/www

%files table-list -f files/table-list
%defattr(644,root,root,755)
%docdir %{_libdir}/m3/www

%files shownew -f files/shownew
%defattr(644,root,root,755)
%docdir %{_libdir}/m3/www

%files gnuemacs -f files/gnuemacs
%defattr(644,root,root,755)
%docdir %{_libdir}/m3/www

%files tempfiles -f files/tempfiles
%defattr(644,root,root,755)
%docdir %{_libdir}/m3/www

%files m3browser -f files/m3browser
%defattr(644,root,root,755)
%docdir %{_libdir}/m3/www

%files web -f files/web
%defattr(644,root,root,755)
%docdir %{_libdir}/m3/www

%files formsvbt -f files/formsvbt
%defattr(644,root,root,755)
%docdir %{_libdir}/m3/www

%files columns -f files/columns
%defattr(644,root,root,755)
%docdir %{_libdir}/m3/www

%files synloc -f files/synloc
%defattr(644,root,root,755)
%docdir %{_libdir}/m3/www

%files pp -f files/pp
%defattr(644,root,root,755)
%docdir %{_libdir}/m3/www

%files fours -f files/fours
%defattr(644,root,root,755)
%docdir %{_libdir}/m3/www

%files m3textohtml -f files/m3textohtml
%defattr(644,root,root,755)
%docdir %{_libdir}/m3/www

%files board -f files/board
%defattr(644,root,root,755)
%docdir %{_libdir}/m3/www

%files vocgi -f files/vocgi
%defattr(644,root,root,755)
%docdir %{_libdir}/m3/www

%files m3tohtml -f files/m3tohtml
%defattr(644,root,root,755)
%docdir %{_libdir}/m3/www

%files smalldb -f files/smalldb
%defattr(644,root,root,755)
%docdir %{_libdir}/m3/www
