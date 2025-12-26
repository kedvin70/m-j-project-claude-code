// Konfigurace asistentů a jejich schopností
const assistants = [
    {
        id: 'code-helper',
        name: 'Kódovací Asistent',
        icon: '💻',
        description: 'Pomáhá s programováním, debugováním a optimalizací kódu',
        detailedDescription: 'Specializovaný asistent pro vývoj software. Umí analyzovat kód, navrhovat řešení, hledat chyby a optimalizovat výkon aplikací.',
        status: 'online',
        colorStart: '#6366f1',
        colorEnd: '#8b5cf6',
        tags: ['Python', 'JavaScript', 'Debug', 'Optimalizace'],
        features: [
            'Psaní a refaktoring kódu',
            'Nalezení a oprava chyb',
            'Optimalizace výkonu',
            'Návrh architektury',
            'Code review'
        ]
    },
    {
        id: 'data-analyst',
        name: 'Datový Analytik',
        icon: '📊',
        description: 'Analyzuje data, vytváří vizualizace a reporty',
        detailedDescription: 'Expert na zpracování a analýzu dat. Vytváří přehledy, grafy a pomáhá s interpretací dat pro business rozhodování.',
        status: 'online',
        colorStart: '#10b981',
        colorEnd: '#059669',
        tags: ['SQL', 'Excel', 'Vizualizace', 'Statistika'],
        features: [
            'Analýza datových setů',
            'Vytváření grafů a dashboardů',
            'SQL dotazy',
            'Statistické výpočty',
            'Business intelligence'
        ]
    },
    {
        id: 'writer',
        name: 'Copywriter',
        icon: '✍️',
        description: 'Tvorba textů, článků a marketingových materiálů',
        detailedDescription: 'Kreativní asistent pro tvorbu všech typů textového obsahu. Od blogů přes e-maily až po marketingové kampaně.',
        status: 'online',
        colorStart: '#f59e0b',
        colorEnd: '#d97706',
        tags: ['Blog', 'Marketing', 'SEO', 'Social Media'],
        features: [
            'Psaní článků a blogů',
            'Marketingové texty',
            'SEO optimalizace',
            'Social media posty',
            'E-mailové kampaně'
        ]
    },
    {
        id: 'designer',
        name: 'UI/UX Designer',
        icon: '🎨',
        description: 'Návrh uživatelských rozhraní a design systémů',
        detailedDescription: 'Pomáhá s návrhem uživatelských rozhraní, vytváří design systémy a poskytuje doporučení pro lepší UX.',
        status: 'busy',
        colorStart: '#ec4899',
        colorEnd: '#db2777',
        tags: ['Figma', 'Design System', 'Prototyping', 'UX'],
        features: [
            'Návrh UI komponent',
            'Vytváření design systémů',
            'Wireframing',
            'Uživatelské testování',
            'Accessibility audit'
        ]
    },
    {
        id: 'devops',
        name: 'DevOps Engineer',
        icon: '🔧',
        description: 'Správa infrastruktury, CI/CD a deployment',
        detailedDescription: 'Specialista na automatizaci, kontejnerizaci a správu cloud infrastruktury. Pomáhá s nastavením CI/CD pipeline.',
        status: 'online',
        colorStart: '#3b82f6',
        colorEnd: '#2563eb',
        tags: ['Docker', 'Kubernetes', 'CI/CD', 'AWS'],
        features: [
            'Nastavení CI/CD pipeline',
            'Kontejnerizace aplikací',
            'Cloud infrastruktura',
            'Monitoring a logging',
            'Automatizace deploymentu'
        ]
    },
    {
        id: 'security',
        name: 'Bezpečnostní Expert',
        icon: '🔒',
        description: 'Audit bezpečnosti, penetrační testy a ochrana dat',
        detailedDescription: 'Specializuje se na kybernetickou bezpečnost, provádí audity, hledá zranitelnosti a doporučuje bezpečnostní opatření.',
        status: 'online',
        colorStart: '#ef4444',
        colorEnd: '#dc2626',
        tags: ['Security', 'Penetration Testing', 'OWASP', 'Encryption'],
        features: [
            'Bezpečnostní audit kódu',
            'Penetrační testování',
            'Analýza zranitelností',
            'GDPR compliance',
            'Šifrování dat'
        ]
    },
    {
        id: 'project-manager',
        name: 'Projektový Manažer',
        icon: '📋',
        description: 'Plánování projektů, řízení týmu a reportování',
        detailedDescription: 'Pomáhá s organizací projektů, vytváří časové plány, sleduje progress a koordinuje týmovou spolupráci.',
        status: 'online',
        colorStart: '#8b5cf6',
        colorEnd: '#7c3aed',
        tags: ['Agile', 'Scrum', 'Jira', 'Planning'],
        features: [
            'Plánování sprintů',
            'Vytváření roadmap',
            'Sledování tasků',
            'Risk management',
            'Týmová koordinace'
        ]
    },
    {
        id: 'ai-ml',
        name: 'AI/ML Specialist',
        icon: '🤖',
        description: 'Strojové učení, AI modely a datová věda',
        detailedDescription: 'Expert na umělou inteligenci a strojové učení. Pomáhá s tréninkem modelů, zpracováním dat a implementací AI řešení.',
        status: 'online',
        colorStart: '#06b6d4',
        colorEnd: '#0891b2',
        tags: ['TensorFlow', 'PyTorch', 'NLP', 'Computer Vision'],
        features: [
            'Trénink ML modelů',
            'NLP zpracování',
            'Computer vision',
            'Prediktivní analýza',
            'AI optimalizace'
        ]
    },
    {
        id: 'database',
        name: 'Databázový Architekt',
        icon: '🗄️',
        description: 'Návrh databází, optimalizace dotazů a správa dat',
        detailedDescription: 'Specialista na databázové systémy. Navrhuje schémata, optimalizuje dotazy a stará se o výkon databází.',
        status: 'busy',
        colorStart: '#84cc16',
        colorEnd: '#65a30d',
        tags: ['PostgreSQL', 'MongoDB', 'Redis', 'Performance'],
        features: [
            'Návrh DB schémat',
            'Optimalizace dotazů',
            'Indexování',
            'Migrace dat',
            'Backup strategie'
        ]
    }
];
