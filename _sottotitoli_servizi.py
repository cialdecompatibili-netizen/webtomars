# -*- coding: utf-8 -*-
"""Aggiunge 'sottotitolo:' ai servizi che non lo hanno (la tab di /servizi/ mostra titolo + sottotitolo). Binario, a-capo preservati, idempotente."""
import os, re, sys
DRY = '--dry' in sys.argv
S = {
'agenti-ai-customer-service': 'Risposte a clienti su chat, email e WhatsApp',
'agenti-ai-per-aziende': 'Assistenza, vendite e processi interni',
'agenti-ai-per-vendite': 'Contatti, appuntamenti e follow-up',
'agenti-ai-vocali': 'Chiamate gestite con passaggio a una persona',
'ai-commerce': 'Schede prodotto, ricerca e assistenza clienti',
'amazon-seo': 'Schede prodotto che si trovano e convincono',
'analisi-competitiva-con-ai': 'Concorrenti, prezzi e posizionamento',
'analisi-predittiva-e-reporting-ai': 'Previsioni e report automatici',
'audit-di-sicurezza-del-sito': 'Vulnerabilità, accessi e punti deboli',
'audit-seo-del-sito': 'Analisi completa e interventi in ordine di priorità',
'backup-e-ripristino-del-sito': 'Copie verificate e ripartenza rapida',
'blog': 'Strategia e articoli per farsi trovare',
'brand-identity': 'Nome, logo, colori e tono di voce',
'brand-voice-ai': 'Il tono del marchio per gli strumenti AI',
'chatbot-e-assistenti-virtuali': 'Risposte ai clienti sui tuoi contenuti',
'cms-custom': 'Pannelli di gestione sul tuo modo di lavorare',
'consulenza-ecommerce': 'Catalogo, margini e percorso d\'acquisto',
'consulenza-seo': 'Audit, parole chiave e piano contenuti',
'content-creation-e-marketing': 'Contenuti scritti, visivi e video',
'copy-multilingua-con-ai': 'Testi in più lingue, rivisti da una persona',
'cro-con-ai': 'Più richieste e acquisti dal sito',
'dashboard-e-business-intelligence': 'Indicatori aggiornati in un colpo d\'occhio',
'data-strategy': 'Quali dati raccogliere e come usarli',
'email-e-crm-automation': 'Sequenze, solleciti e recupero clienti',
'firewall-e-protezione-dagli-attacchi': 'Filtri anti-bot e difesa dagli attacchi',
'frontend-editing': 'Grafica e layout senza rifare tutto',
'grafica-per-social': 'Modelli coordinati per post e storie',
'influencer-marketing': 'Creator giusti e collaborazioni chiare',
'infografica-e-grafica-animata': 'Dati e idee spiegati con le immagini',
'landing-page-e-funnel': 'Pagine pensate per un\'azione precisa',
'lead-scoring-con-ai': 'Un punteggio per ogni contatto',
'link-building-e-digital-pr': 'Citazioni e link guadagnati sul web',
'local-seo-google-my-business': 'Farsi trovare da chi cerca vicino',
'manutenzione-e-infrastruttura': 'Aggiornamenti, backup e assistenza',
'marketing-per-professionisti': 'Studi e liberi professionisti',
'monitoraggio-e-aggiornamenti-di-sicurezza': 'Controllo continuo e avvisi tempestivi',
'personalizzazione-1-to-1': 'Contenuti e offerte su misura per ogni cliente',
'podcast': 'Dal formato alla pubblicazione',
'ppc-per-ecommerce': 'Shopping, Performance Max e social',
'protezione-wordpress-e-cms': 'Aggiornamenti, permessi e accessi',
'pulizia-malware-e-delisting': 'Sito pulito e avvisi Google rimossi',
'reputazione-online': 'Recensioni, risposte e presenza su Google',
'restyling-del-sito': 'Nuova grafica senza perdere visibilità',
'seo-copywriting': 'Testi chiari, utili e ottimizzati',
'seo-per-aziende': 'B2B e PMI, misurato sui contatti',
'seo-per-ecommerce': 'Schede, categorie e catalogo',
'sicurezza-account-e-accessi': 'Password, doppio fattore e permessi',
'siti-mobile-e-web-app': 'Veloci da telefono, collegati ai tuoi sistemi',
'siti-web-aziendali-e-portali': 'Veloci, accessibili e facili da aggiornare',
'sito-multilingua': 'SEO internazionale e testi per ogni paese',
'social-ads-per-ecommerce': 'Meta e TikTok dal catalogo',
'social-media-marketing': 'Strategia, piano editoriale e community',
'sviluppo-su-misura': 'Applicazioni, gestionali e integrazioni',
'tiktok-ads': 'Video verticali e Spark Ads',
'ui-ux-design': 'Esperienza d\'uso e interfaccia testate',
'video-marketing': 'Idee, riprese, montaggio e distribuzione',
'visual-ai-su-larga-scala': 'Immagini in serie con stile coerente',
'web-analytics-e-cro': 'Misura corretta e test per convertire',
'web-design': 'Siti chiari, veloci e coerenti col marchio',
}
ok = 0; salt = []
for slug, sub in S.items():
    p = os.path.join('_servizi', slug + '.md')
    if not os.path.exists(p): salt.append(slug); continue
    raw = open(p, 'rb').read(); bom = raw.startswith(b'\xef\xbb\xbf')
    t = raw.decode('utf-8-sig'); nl = '\r\n' if '\r\n' in t else '\n'
    m = re.match(r'(---\r?\n)(.*?)(\r?\n---)', t, re.S)
    if not m: salt.append(slug); continue
    fm = m.group(2)
    if re.search(r'(?m)^sottotitolo:\s*\S', fm): salt.append(slug + '(gia)'); continue
    assert ':' not in sub, sub
    righe = fm.split(nl)
    righe = [r for r in righe if not re.match(r'sottotitolo:\s*$', r)]
    idx = max([i for i, r in enumerate(righe) if re.match(r'(gruppo|ordine):', r)] or [len(righe) - 1])
    righe.insert(idx + 1, 'sottotitolo: ' + sub)
    n = t[:m.start(2)] + nl.join(righe) + t[m.end(2):]
    if not DRY: open(p, 'wb').write((b'\xef\xbb\xbf' if bom else b'') + n.encode('utf-8'))
    ok += 1
print('aggiornati', ok, '| saltati', salt)
