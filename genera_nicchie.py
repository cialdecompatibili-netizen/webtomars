"""genera_nicchie.py - crea/riordina le pagine "Siti su misura per nicchia" in _servizi/.

USO:  python genera_nicchie.py   (poi: git add _servizi; git commit; git push)

COME AGGIUNGERE UNA NICCHIA (basta 2 passi, il resto e' automatico):
  1) aggiungi lo slug in ORDER nella posizione voluta (1 = piu' profittevole)
  2) aggiungi la voce in NEW con lo stesso slug (testi: vedi sotto)
Lo script e' IDEMPOTENTE: i file gia' esistenti NON vengono riscritti (cosi' non perde
modifiche manuali), viene solo rinumerato 'ordine:' secondo ORDER.

PUNTI CRITICI:
  - 'gruppo' deve essere ESATTAMENTE GR: e' la stringa con cui la pagina /servizi/ raggruppa le card.
  - 'ordine' deve essere unico nel gruppo: lo calcola lo script da ORDER, non scriverlo a mano nei file.
  - Testi: niente promesse di risultati o cifre. Professioni regolamentate (medici, notai, avvocati,
    psicologi...): FAQ sulle regole dell'ordine, verifica finale a carico del cliente.
  - File scritti con LF e UTF-8 (git su Windows avvisa su CRLF: e' normale).
  - sito-per-creator.md e' di un altro gruppo ("Creator e YouTube"): NON va in ORDER.

FONTI DELL'ORDINE (indicatori di capacita' di spesa, non dati di domanda di siti):
  IT: Fiscozen su 40mila P.IVA (money.it, gen 2026; fanpage.it) - medici specialisti, elettricisti
      impiantisti, ingegneri, creator in testa; consulenti, pubblicitari, psicologi tra le piu' ambite.
  IT: Osservatorio entrate fiscali 2025 / businessonline.it - notai, commercialisti, consulenti del lavoro.
  DE: Accountable su 30mila autonomi (dic 2025) - in testa Immobilien/Finanzmakler (~84mila euro),
      poi consulenti, ingegneri, IT; in fondo fotografi e beauty. Psicologi in Italia 15-25mila euro: bassi.
Per l'aggiornamento: rifare la ricerca ogni 6-12 mesi e riordinare ORDER.
"""
import re, pathlib
# Cartella dei servizi (percorso assoluto: lo script gira solo su questo PC)
D = pathlib.Path(r"C:\Users\mirco\Desktop\repository\webtomars\_servizi")
GR = "Siti su misura per nicchia"  # CRITICO: stringa identica al front matter 'gruppo'
# Ordine di profittabilita' stimata (dalla piu' alta). L'indice + 1 diventa 'ordine:' nel front matter.
ORDER = ["medici-specialisti","avvocati-e-studi-legali","dentisti-e-studi-medici","commercialisti-e-consulenti",
"consulenti-del-lavoro","installatori-fotovoltaico-e-climatizzazione","ingegneri-e-periti-industriali",
"sviluppatori-e-consulenti-it","agenti-assicurativi","agenti-immobiliari","mediatori-creditizi-e-consulenti-finanziari",
"consulenti-aziendali-e-gestionali","agenzie-marketing-e-pubblicita","artigiani-e-imprese-edili",
"architetti-e-studi-tecnici","elettricisti-e-impiantisti","produzioni-video-e-agenzie","coach-e-formatori",
"farmacie-e-parafarmacie","fisioterapisti-e-osteopati","veterinari-e-toelettature",
"autofficine-e-carrozzerie","bnb-e-case-vacanza","wedding-planner-ed-eventi","ncc-e-noleggio-con-conducente",
"ristoranti-e-pizzerie","parrucchieri-e-centri-estetici","personal-trainer-e-palestre","fotografi-e-videomaker",
"psicologi-e-psicoterapeuti","chef-e-cuochi","scuole-guida","imprese-di-pulizie-e-traslochi","scuole-di-danza-e-musica","notai"]
# slug: (nome, a chi, sottotitolo, include[5], faq_q, faq_a)
NEW = {
"medici-specialisti": ("medici specialisti","medici specialisti e studi di diagnostica","Il tuo studio, presentato con chiarezza",
 ["Presentazione del medico, delle specializzazioni e delle prestazioni","Schede chiare per ogni visita ed esame","Richiesta di appuntamento o contatto con la segreteria","Informativa privacy e gestione dei consensi","Articoli informativi, se vuoi farti trovare su Google"],
 "Il sito rispetta le regole sulla pubblicità sanitaria?","Impostiamo i contenuti in modo informativo e senza promesse di risultato; la verifica finale sulle regole del tuo ordine resta tua."),
"agenti-assicurativi": ("agenti assicurativi","agenti assicurativi e agenzie di assicurazione","Un punto di contatto chiaro per i tuoi clienti",
 ["Presentazione dell'agenzia e del mandato","Aree di copertura spiegate in modo semplice","Richiesta di preventivo o consulenza","Riferimenti e orari dell'agenzia","Articoli di approfondimento, se vuoi farti trovare su Google"],
 "Posso indicare le compagnie con cui lavoro?","Sì, inseriamo le informazioni che ci dai, rispettando le regole di trasparenza del settore."),
"ingegneri-e-periti-industriali": ("ingegneri e periti industriali","ingegneri, periti industriali e studi di ingegneria","Competenze tecniche spiegate bene",
 ["Presentazione dello studio e delle competenze","Schede dei servizi (progettazione, collaudi, perizie, pratiche)","Esempi di lavori svolti, se vuoi mostrarli","Richiesta di preventivo","Articoli tecnici, se vuoi farti trovare su Google"],
 "Posso mostrare i miei progetti?","Sì, scegliamo insieme quali lavori presentare, nel rispetto della riservatezza dei clienti."),
"consulenti-aziendali-e-gestionali": ("consulenti aziendali e gestionali","consulenti aziendali, gestionali e formatori","Il tuo metodo, in modo credibile",
 ["Presentazione del consulente e del metodo di lavoro","Servizi descritti per tipo di cliente","Richiesta di un primo incontro","Contenuti e articoli, se vuoi farti trovare su Google","Area per eventuali corsi o formazione"],
 "Posso inserire casi o testimonianze?","Sì, se hai il consenso dei clienti; senza consenso li lasciamo anonimi o fuori."),
"elettricisti-e-impiantisti": ("elettricisti e impiantisti elettrici","elettricisti, impiantisti e installatori","Presenza locale per chi cerca un impiantista",
 ["Presentazione dell'impresa e delle zone servite","Schede dei servizi (impianti civili, industriali, domotica, pratiche)","Richiesta di sopralluogo o preventivo","Pagine per zona, utili alla ricerca locale","Riferimenti e orari ben visibili"],
 "Il sito mi aiuta a farmi trovare nella mia zona?","Strutturiamo le pagine per ricerca locale; la posizione su Google dipende poi da molti fattori."),
"produzioni-video-e-agenzie": ("produzioni video e agenzie","produzioni video, case di produzione e agenzie creative","Il tuo portfolio in primo piano",
 ["Portfolio con video e progetti scelti","Schede dei servizi (spot, corporate, eventi, post-produzione)","Richiesta di preventivo","Pagina del team e dell'attrezzatura","Caricamento leggero anche con molti contenuti"],
 "Posso incorporare i video da YouTube o Vimeo?","Sì, incorporiamo i video mantenendo il sito veloce."),
"farmacie-e-parafarmacie": ("farmacie e parafarmacie","farmacie e parafarmacie","Servizi e orari sempre a portata di mano",
 ["Presentazione della farmacia e dei servizi (analisi, prenotazioni, consegne)","Orari e turni ben visibili","Contatti e indicazioni per raggiungerti","Eventuale vetrina di prodotti e novità","Informativa privacy e gestione dei consensi"],
 "Posso mostrare i turni e gli orari?","Sì, li rendiamo facili da aggiornare."),
"consulenti-del-lavoro": ("consulenti del lavoro","consulenti del lavoro e studi paghe","Paghe e contributi, spiegati in modo semplice",
 ["Presentazione dello studio e dei servizi (paghe, contributi, assunzioni)","Schede per tipo di cliente (imprese, artigiani, professionisti)","Richiesta di consulenza","Scadenze e novità, se vuoi pubblicarle","Informativa privacy e gestione dei consensi"],
 "Posso pubblicare aggiornamenti su scadenze e novità?","Sì, con articoli semplici da aggiornare, utili anche per farti trovare su Google."),
"sviluppatori-e-consulenti-it": ("sviluppatori e consulenti IT","sviluppatori freelance, consulenti IT e software house","Competenze e progetti in evidenza",
 ["Presentazione delle competenze e delle tecnologie","Portfolio di progetti e casi d'uso","Richiesta di preventivo o call","Pagina servizi (sviluppo, integrazioni, assistenza)","Sito veloce e curato nel codice"],
 "Posso mostrare progetti coperti da riservatezza?","Sì, li presentiamo in forma anonima o generica, secondo gli accordi con i clienti."),
"mediatori-creditizi-e-consulenti-finanziari": ("mediatori creditizi e consulenti finanziari","mediatori creditizi, consulenti finanziari e agenzie di intermediazione","Fiducia e trasparenza fin dal primo contatto",
 ["Presentazione del professionista e delle iscrizioni agli albi","Servizi spiegati in modo semplice","Richiesta di consulenza","Informazioni di trasparenza richieste dal settore","Informativa privacy e gestione dei consensi"],
 "Il sito rispetta le regole di trasparenza del settore?","Inseriamo le informazioni obbligatorie che ci fornisci e non promettiamo rendimenti; la verifica finale resta tua."),
"agenzie-marketing-e-pubblicita": ("agenzie di marketing e pubblicità","agenzie di marketing, pubblicità e comunicazione","Un'agenzia che si presenta con il suo stesso sito",
 ["Presentazione dell'agenzia e del metodo","Portfolio di campagne e progetti","Schede dei servizi (strategia, social, SEO, contenuti)","Richiesta di preventivo","Blog per i tuoi contenuti"],
 "Posso mostrare campagne per clienti?","Sì, scegliamo insieme i casi da presentare, con il consenso dei clienti."),
"coach-e-formatori": ("coach e formatori","coach, formatori e consulenti di crescita personale e professionale","Il tuo percorso, presentato con chiarezza",
 ["Presentazione del coach e del metodo","Percorsi, corsi e workshop descritti per obiettivo","Richiesta di un primo colloquio","Calendario degli eventi, se ne hai","Articoli e contenuti, se vuoi farti trovare su Google"],
 "Posso inserire testimonianze?","Sì, con il consenso di chi le ha scritte e senza promettere risultati."),
"notai": ("notai","notai e studi notarili","Un sito sobrio per lo studio",
 ["Presentazione dello studio e dei servizi","Informazioni sulle pratiche più comuni","Richiesta di appuntamento","Contatti e orari","Informativa privacy"],
 "Il sito rispetta le regole della professione?","Impostiamo i contenuti in modo informativo e sobrio; la verifica finale sulle regole del tuo ordine resta tua."),
}
def body(n, who, inc, q, a):
    return f"""Un sito generico non basta quando lavori in un settore preciso: i tuoi clienti cercano cose precise, con parole precise. Per questo realizziamo un **sito per {n}** pensato per {who}.

## Cosa include

""" + "\n".join("- "+i for i in inc) + f"""

## Come lavoriamo

Partiamo dal tuo modo di lavorare: servizi, clienti tipo, zona e tono di voce. Poi scegliamo struttura, testi e immagini, e ti consegniamo un sito veloce, adatto a smartphone e semplice da aggiornare. Dopo la pubblicazione restiamo disponibili per modifiche e manutenzione.

## Domande frequenti

**{q}**

{a}

Vuoi vedere come sarebbe il tuo sito? [Contattaci](/contatti/) per una prima consulenza gratuita.
"""
for i, s in enumerate(ORDER, 1):
    f = D / f"sito-per-{s}.md"
    # Nuova nicchia: crea il file solo se NON esiste (idempotente, non sovrascrive modifiche manuali)
    if s in NEW and not f.exists():
        n, who, sub, inc, q, a = NEW[s]
        desc = f"Sito per {n} su misura: {sub[0].lower()+sub[1:]}. Pensato per {who}. Prima consulenza gratuita."
        t = f"""---
layout: servizio
title: Sito per {n}
description: "{desc}"
gruppo: {GR}
ordine: {i}
sottotitolo: {sub}
seo_title: Sito per {n} - Smart Web Agency
seo_description: "{desc}"
---

""" + body(n, who, inc, q, a)
        f.write_text(t, encoding="utf-8", newline="\n")
    else:
        # File esistente: si rinumera solo 'ordine:' (prima occorrenza = front matter)
        t = f.read_text(encoding="utf-8")
        t = re.sub(r"(?m)^ordine: \d+$", f"ordine: {i}", t, count=1)
        f.write_text(t, encoding="utf-8", newline="\n")
print("ok", len(ORDER))
