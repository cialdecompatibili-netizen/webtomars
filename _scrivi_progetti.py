# -*- coding: utf-8 -*-
"""Riscrive/aggiunge le schede in _projects/ (testi da web agency, SENZA tecnologie, hosting o URL interni) e aggiunge l'intro a /projects/.
Dati ricavati dai siti online. UTF-8 senza BOM, CRLF. Idempotente. Uso: python _scrivi_progetti.py [--dry]"""
import os, sys
DRY = "--dry" in sys.argv
BASE = os.path.dirname(os.path.abspath(__file__))

def scheda(titolo, desc, imp, home, intro, url, dom, fatto, esito):
    righe = ["---", "layout: page", 'title: "%s"' % titolo, 'description: "%s"' % desc, "importance: %d" % imp,
             "category: work", "in_home: %s" % ("true" if home else "false"), "---", "", intro, "",
             '<p><a class="btn btn-primary" href="%s" target="_blank" rel="noopener">Visita il sito %s</a></p>' % (url, dom), "",
             "### Cosa abbiamo fatto", ""]
    righe += ["- **%s**: %s" % (a, b) for a, b in fatto]
    righe += ["", "### Il risultato", "", esito, ""]
    return "\n".join(righe)

SCHEDE = {
"diavolopiccante": scheda("Diavolo Piccante", "Sito, shop e magazine di un'azienda agricola del peperoncino", 1, True,
 "**Diavolo Piccante** è un'azienda agricola specializzata in prodotti piccanti, sementi, salse e orto. Abbiamo costruito il suo spazio online come un vero **negozio con una redazione dentro**: chi arriva può acquistare e, nello stesso posto, informarsi.",
 "https://diavolopiccante.it/", "diavolopiccante.it",
 [("Negozio online", "catalogo di peperoncini, salse, sementi e prodotti dell'orto, con schede prodotto curate e un percorso d'acquisto semplice, da computer e da smartphone."),
  ("Contenuti editoriali", "guide, ricette, curiosità e un'enciclopedia del peperoncino: contenuti utili che accompagnano il cliente e fanno conoscere il marchio."),
  ("Visibilità sui motori di ricerca", "struttura delle pagine, titoli e descrizioni pensati per farsi trovare da chi cerca prodotti e informazioni sul peperoncino."),
  ("Immagine coerente", "uno stile riconoscibile dal negozio agli articoli, per far percepire la qualità di un'azienda agricola vera."),
  ("Gestione continua", "aggiornamento di prodotti e contenuti, controlli periodici e interventi rapidi quando serve.")],
 "Un sito che unisce vendita e informazione: il cliente scopre, si fida e acquista, mentre l'azienda cresce nel tempo con nuovi contenuti."),
"italianchilli": scheda("ItalianChilli", "Sito e shop online di un'azienda agricola alle porte di Roma", 1, True,
 "**ItalianChilli** è un'azienda agricola alle porte di Roma che coltiva e trasforma peperoncino. Per lei abbiamo realizzato un sito che racconta la realtà produttiva e un **negozio online** per portare i prodotti direttamente nelle case dei clienti.",
 "https://italianchilli.com/", "italianchilli.com",
 [("Sito di presentazione", "la storia dell'azienda, la filosofia di lavoro e la gamma dei prodotti, con un tono genuino e vicino al territorio."),
  ("Shop online", "catalogo ordinato per categorie, schede prodotto chiare e acquisto in pochi passaggi."),
  ("Fotografia e immagine", "scelta e cura delle immagini per valorizzare i prodotti e rendere il marchio riconoscibile."),
  ("Posizionamento", "testi e struttura ottimizzati per i motori di ricerca, in modo da farsi trovare da chi cerca peperoncino e specialità piccanti."),
  ("Assistenza", "supporto continuo per aggiornare listino, offerte e contenuti.")],
 "Un'azienda agricola che oggi ha una vetrina professionale aperta 24 ore su 24 e un canale di vendita diretto, senza intermediari."),
"royalchilli": scheda("Royal Chilli", "E-commerce di prodotti al peperoncino", 1, True,
 "**Royal Chilli** è un negozio online dedicato al mondo del peperoncino. L'obiettivo era semplice: far trovare i prodotti, far capire subito cosa distingue il marchio e rendere l'acquisto facile.",
 "https://royalchili.com/", "royalchili.com",
 [("Negozio online completo", "catalogo, categorie, carrello e ordine pensati per chi compra da telefono come da computer."),
  ("Schede prodotto efficaci", "descrizioni, immagini e informazioni organizzate per aiutare la decisione d'acquisto."),
  ("Immagine di marca", "uno stile unico e riconoscibile su tutte le pagine, dal catalogo ai contatti."),
  ("Ottimizzazione per i motori di ricerca", "struttura e testi curati perché il negozio sia trovato da chi cerca proprio quei prodotti."),
  ("Manutenzione", "aggiornamenti costanti e controlli per mantenere il negozio veloce e sicuro.")],
 "Una vetrina online ordinata, riconoscibile e pronta a vendere, che può crescere con nuovi prodotti e nuove categorie."),
"spicy-devil": scheda("Spicy Devil", "Shop internazionale di semi di peperoncino, peperoncini secchi e polveri", 1, False,
 "**Spicy Devil** vende semi premium, peperoncini secchi e polveri di peperoncino a un pubblico appassionato. Abbiamo creato un negozio pensato per chi cerca la qualità e vuole imparare: accanto al catalogo c'è un **blog con consigli e ricette**.",
 "http://spicy-devil.com/", "spicy-devil.com",
 [("Negozio online", "catalogo di semi, peperoncini essiccati e polveri, con schede chiare e un acquisto semplice."),
  ("Contenuti per gli appassionati", "blog con consigli di coltivazione e ricette, per accompagnare il cliente prima e dopo l'acquisto."),
  ("Taglio internazionale", "testi e struttura pensati per essere compresi e trovati anche da chi cerca in inglese."),
  ("Visibilità organica", "titoli, descrizioni e organizzazione delle pagine curati per i motori di ricerca."),
  ("Assistenza continua", "aggiornamento del catalogo e dei contenuti nel tempo.")],
 "Un negozio specializzato che parla la lingua degli appassionati e usa i contenuti per portare nuovi clienti."),
"florbook": scheda("Florbook", "Catalogo digitale e shop di semi, ortaggi, erbe aromatiche e fiori", 1, True,
 "**Florbook** è un catalogo digitale di semi, ortaggi, erbe aromatiche e fiori, affiancato da guide pratiche su semina, coltivazione e ricette. Un progetto che mette insieme **vendita e informazione** per chi ama l'orto e il giardino.",
 "https://florbook.com/", "florbook.com",
 [("Catalogo e negozio", "un ampio catalogo organizzato per tipo di pianta e di utilizzo, per trovare subito ciò che serve."),
  ("Guide di semina e coltivazione", "contenuti utili e ben strutturati che rispondono alle domande di chi coltiva."),
  ("Ricette e idee", "una parte editoriale che fa scoprire come usare in cucina quello che si coltiva."),
  ("Visibilità sui motori di ricerca", "schede e articoli pensati per farsi trovare da chi cerca semi, orto e giardinaggio."),
  ("Aggiornamento continuo", "nuovi prodotti, nuove guide e miglioramenti nel tempo.")],
 "Una risorsa unica per l'orto e il giardino, in cui il catalogo e i contenuti si sostengono a vicenda."),
"italianprice": scheda("Italian Price", "Shop di prodotti tipici italiani per il mercato estero", 2, False,
 "**Italian Price** porta le specialità italiane ai clienti di tutto il mondo. Un negozio in inglese, pensato per chi cerca prodotti tipici autentici e vuole acquistarli senza complicazioni.",
 "https://italianprice.com/", "italianprice.com",
 [("Negozio in lingua inglese", "testi, categorie e percorso d'acquisto progettati per un pubblico internazionale."),
  ("Catalogo di prodotti tipici", "schede curate per raccontare l'origine e la qualità di ogni specialità."),
  ("Immagine coerente", "uno stile semplice e riconoscibile che richiama l'eccellenza italiana."),
  ("Posizionamento", "struttura e contenuti ottimizzati per le ricerche internazionali sui prodotti italiani.")],
 "Una vetrina internazionale dedicata al gusto italiano, pronta a crescere con nuovi prodotti e nuovi mercati."),
"villatrecolli": scheda("Villa Tre Colli", "Sito bilingue di una location per eventi a Monterotondo", 1, True,
 "**Villa Tre Colli** è una location per eventi a Monterotondo, alle porte di Roma. Per lei abbiamo realizzato un sito completo e bilingue, italiano e inglese, che racconta gli spazi e guida chi organizza un evento fino alla richiesta di contatto.",
 "https://villatrecolli.com/", "villatrecolli.com",
 [("Pagine per ogni tipo di evento", "matrimoni, matrimoni civili, battesimi, comunioni e cresime, compleanni e feste a tema, meeting aziendali."),
  ("Spazi e servizi", "la villa, le sale, lo spazio esterno, la cucina interna, il catering, l'animazione e la musica, i servizi inclusi."),
  ("Versione in inglese", "tutte le pagine tradotte, per intercettare anche chi organizza dall'estero."),
  ("Galleria fotografica", "immagini curate per far percepire l'atmosfera del luogo prima ancora di visitarlo."),
  ("Visibilità e immagine", "titoli, testi e struttura pensati per i motori di ricerca e uno stile coerente con il prestigio della villa."),
  ("Contatti semplici", "moduli e percorsi chiari per chiedere un preventivo o fissare una visita.")],
 "Un sito che fa da biglietto da visita, brochure e primo contatto commerciale in un unico posto, in due lingue."),
"edilextreme": scheda("Edilextreme", "Sito web e SEO per lavori su fune ed edilizia acrobatica", 1, True,
 "**Edilextreme** offre servizi di edilizia e lavori su fune a Roma e nel Lazio. Per lei abbiamo costruito un sito pensato per essere trovato da chi ha un'urgenza concreta e cerca un'impresa affidabile nella propria zona.",
 "https://edilextreme.com/", "edilextreme.com",
 [("Pagine per servizio e per zona", "ogni lavoro e ogni territorio ha la sua pagina, per rispondere esattamente a ciò che l'utente cerca."),
  ("SEO basata sui dati", "ottimizzazione dei contenuti sulla base di ciò che le persone cercano davvero, con controlli periodici dei risultati."),
  ("Testi chiari e concreti", "spiegazioni semplici dei lavori, dei tempi e dei vantaggi, senza gergo inutile."),
  ("Percorso di contatto", "richieste di preventivo facili da inviare da telefono, il canale più usato in questo settore.")],
 "Un sito costruito per generare richieste, non solo per essere visto."),
"italfuni": scheda("Italfuni", "Sito web e SEO per lavori su fune e manutenzione in quota", 1, True,
 "**Italfuni** si occupa di lavori su fune e manutenzione in quota. Abbiamo realizzato un sito mirato che spiega con chiarezza cosa viene fatto, dove e in quali situazioni è la soluzione giusta.",
 "https://italfuni.it/", "italfuni.it",
 [("Pagine per servizio e per zona", "ogni lavorazione ha la sua pagina e ogni area di intervento un riferimento locale."),
  ("SEO e contenuti", "testi e struttura curati per essere trovati da chi cerca interventi in quota."),
  ("Immagine professionale", "uno stile sobrio e affidabile, coerente con un lavoro dove la sicurezza è tutto."),
  ("Contatto immediato", "un percorso rapido per richiedere un sopralluogo o un preventivo.")],
 "Un sito chiaro e credibile che trasforma le ricerche locali in richieste di intervento."),
"ipermark": scheda("Ipermark", "Sito web e piattaforma online", 2, False,
 "**Ipermark** è il nostro progetto di piattaforma online: un sito costruito per presentare soluzioni digitali e dare ai clienti un punto di riferimento chiaro.",
 "https://ipermark.com/", "ipermark.com",
 [("Sito e piattaforma", "struttura e contenuti pensati per spiegare in modo semplice l'offerta."),
  ("Immagine coerente", "uno stile unico su tutte le pagine."),
  ("Evoluzione continua", "nuove sezioni e miglioramenti aggiunti nel tempo.")],
 "Una base solida su cui far crescere l'offerta digitale."),
}

INTRO = '''<p class="lead">Ogni progetto parte da un obiettivo di business, non da un modello di sito: capiamo cosa deve ottenere il cliente, progettiamo l'esperienza di chi visita, costruiamo e pubblichiamo, poi misuriamo e miglioriamo. Qui sotto una selezione dei lavori realizzati per e-commerce, aziende di servizi e strutture ricettive.</p>

<p>Per ogni progetto ci occupiamo di <strong>strategia, design, sviluppo, contenuti, visibilità sui motori di ricerca e assistenza continua</strong>: un unico interlocutore dall'idea alla crescita.</p>

'''

def scrivi(path, testo):
    b = testo.replace("\r\n", "\n").replace("\n", "\r\n").encode("utf-8")
    if not DRY:
        open(path, "wb").write(b)

for slug, t in SCHEDE.items():
    scrivi(os.path.join(BASE, "_projects", slug + ".md"), t)
print("schede:", len(SCHEDE))

# intro in _pages/projects.md (solo una volta)
p = os.path.join(BASE, "_pages", "projects.md")
raw = open(p, "rb").read().decode("utf-8")
crlf = "\r\n" in raw
t = raw.replace("\r\n", "\n")
if "Ogni progetto parte da un obiettivo di business" not in t:
    k = t.index("<!-- pages/projects.md -->")
    t = t[:k] + INTRO + t[k:]
    t = t.replace("description: Una collezione in crescita dei tuoi progetti più interessanti.", "description: I progetti realizzati da webtomars: e-commerce, siti per aziende e strutture ricettive.")
    if crlf: t = t.replace("\n", "\r\n")
    if not DRY: open(p, "wb").write(t.encode("utf-8"))
    print("intro aggiunta")
else:
    print("intro gia' presente")

