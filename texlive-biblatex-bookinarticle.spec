%global tl_name biblatex-bookinarticle
%global tl_revision 40323

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.3.1a
Release:	%{tl_revision}.1
Summary:	Manage book edited in article
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/biblatex-contrib/biblatex-bookinarticle
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/biblatex-bookinarticle.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/biblatex-bookinarticle.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
Requires(pre):	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package provides three new BibLaTeX entry types - @bookinarticle,
@bookinincollection and @bookinthesis - to refer to a modern edition of
an old book, where this modern edition is provided in a @article,
@incollection or in a @thesis. The package is now superseded by
biblatex-bookinother.

%prep
%setup -q -c -a1
rm -rf tlpkg
if [ -d RELOC ]; then
	cp -a RELOC/. .
	rm -rf RELOC
fi

%build

%install
mkdir -p %{buildroot}%{_datadir}/texmf-dist
# Flat tlnet layout: tex/ doc/ source/ fonts/ ... -> texmf-dist/
if [ -d texmf-dist ]; then
	cp -a texmf-dist/. %{buildroot}%{_datadir}/texmf-dist/
elif [ -d texmf ]; then
	mkdir -p %{buildroot}%{_datadir}/texmf
	cp -a texmf/. %{buildroot}%{_datadir}/texmf/
else
	for d in * .[!.]* ..?*; do
		[ -e "$d" ] || continue
		case "$d" in tlpkg|RELOC) continue ;; esac
		cp -a "$d" %{buildroot}%{_datadir}/texmf-dist/
	done
fi
rm -rf %{buildroot}%{_datadir}/texmf-dist/tlpkg

%files
%dir %{_datadir}/texmf-dist
%dir %{_datadir}/texmf-dist/doc
%dir %{_datadir}/texmf-dist/tex
%dir %{_datadir}/texmf-dist/doc/latex
%dir %{_datadir}/texmf-dist/tex/latex
%dir %{_datadir}/texmf-dist/doc/latex/biblatex-bookinarticle
%dir %{_datadir}/texmf-dist/tex/latex/biblatex-bookinarticle
%dir %{_datadir}/texmf-dist/doc/latex/biblatex-bookinarticle/documentation
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-bookinarticle/README
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-bookinarticle/documentation/biblatex-bookinarticle-crossref.pdf
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-bookinarticle/documentation/biblatex-bookinarticle.dot
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-bookinarticle/documentation/biblatex-bookinarticle.pdf
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-bookinarticle/documentation/biblatex-bookinarticle.tex
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-bookinarticle/documentation/example-bookinarticle.bib
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-bookinarticle/documentation/example-bookinincollection.bib
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-bookinarticle/documentation/example-bookinthesis.bib
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-bookinarticle/documentation/makefile
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-bookinarticle/makefile
%{_datadir}/texmf-dist/tex/latex/biblatex-bookinarticle/biblatex-bookinarticle.sty
