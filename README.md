# 🤖 Dashboard Asistentů

Centrální dashboard pro výběr a správu AI asistentů řešících konkrétní úkoly.

## 📋 Popis

Tento projekt poskytuje moderní webové rozhraní pro výběr různých typů AI asistentů specializovaných na konkrétní úkoly - od programování přes analýzu dat až po projektový management.

## ✨ Funkce

- **Přehledný dashboard** s dlaždicemi pro každého asistenta
- **Interaktivní karty** s informacemi o schopnostech asistentů
- **Responzivní design** fungující na všech zařízeních
- **Modal okna** s detailními informacemi
- **Barevné kategorizace** asistentů podle typu
- **Status indikátory** (online/busy/offline)

## 🎨 Dostupní asistenti

1. **Kódovací Asistent** 💻 - Programování, debugging, optimalizace
2. **Datový Analytik** 📊 - Analýza dat, vizualizace, reporty
3. **Copywriter** ✍️ - Tvorba textů, marketing, SEO
4. **UI/UX Designer** 🎨 - Návrh rozhraní, design systémy
5. **DevOps Engineer** 🔧 - Infrastruktura, CI/CD, deployment
6. **Bezpečnostní Expert** 🔒 - Audit bezpečnosti, penetrační testy
7. **Projektový Manažer** 📋 - Plánování, řízení, koordinace
8. **AI/ML Specialist** 🤖 - Strojové učení, AI modely
9. **Databázový Architekt** 🗄️ - Návrh DB, optimalizace dotazů

## 🚀 Instalace a spuštění

1. Klonujte repozitář:
```bash
git clone <repository-url>
cd m-j-project-claude-code
```

2. Otevřete `index.html` v prohlížeči:
```bash
# Můžete použít libovolný lokální server, například:
python -m http.server 8000
# nebo
npx serve
```

3. Otevřete v prohlížeči: `http://localhost:8000`

## 📁 Struktura projektu

```
m-j-project-claude-code/
├── index.html              # Hlavní HTML soubor
├── css/
│   └── styles.css         # Styly dashboardu
├── js/
│   ├── app.js            # Hlavní aplikační logika
│   └── assistants-config.js  # Konfigurace asistentů
├── assets/                # Obrázky a další assety
└── README.md             # Tento soubor
```

## 🛠️ Technologie

- **HTML5** - Struktura stránky
- **CSS3** - Styly, grid layout, animace
- **Vanilla JavaScript** - Interaktivita bez frameworků
- **Responzivní design** - Mobile-first přístup

## 📝 Jak přidat nového asistenta

Editujte soubor `js/assistants-config.js` a přidejte nový objekt do pole `assistants`:

```javascript
{
    id: 'unique-id',
    name: 'Jméno asistenta',
    icon: '🎯',
    description: 'Krátký popis',
    detailedDescription: 'Podrobný popis schopností',
    status: 'online', // online, busy, offline
    colorStart: '#hexcolor1',
    colorEnd: '#hexcolor2',
    tags: ['Tag1', 'Tag2'],
    features: [
        'Funkce 1',
        'Funkce 2'
    ]
}
```

## 🎯 Budoucí rozšíření

- [ ] Integrace se skutečnými AI API
- [ ] Vyhledávání a filtrace asistentů
- [ ] Uživatelské účty a historie
- [ ] Chat rozhraní s asistenty
- [ ] Statistiky a analytika použití
- [ ] Vlastní konfigurace asistentů

## 📄 Licence

MIT License

## 👨‍💻 Autor

Vytvořeno s pomocí Claude Code
