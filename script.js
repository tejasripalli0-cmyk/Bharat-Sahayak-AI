// Localization Text Content Matrix
const translations = {
    en: {
        formTitle: "User Demographics",
        age: "Current Age (Years)",
        salary: "Annual Income / Salary ($/₹)",
        gender: "Gender Identity",
        state: "Regional Territory / State",
        occupation: "Professional Occupation Group",
        submit: "Evaluate Profile",
        resultsHeader: "Available Programs & Subsidies",
        placeholder: "Please input your demographic profile matrix on the left panel to execute the eligibility evaluation engine.",
        detailsTitle: "Program Description & Terms",
        docsTitle: "Required Document Verification Checklist"
    },
    te: {
        formTitle: "వినియోగదారు వివరాలు",
        age: "ప్రస్తుత వయస్సు (సంవత్సరాలు)",
        salary: "సంవత్సర ఆదాయం / జీతం ($/₹)",
        gender: "లింగం",
        state: "ప్రాంతీయ భూభాగం / రాష్ట్రం",
        occupation: "వృత్తిపరమైన సమూహం",
        submit: "ప్రొఫైల్ తనిఖీ చేయండి",
        resultsHeader: "అందుబాటులో ఉన్న పథకాలు & సబ్సిడీలు",
        placeholder: "అర్హత మూల్యాంకన ఇంజిన్‌ను అమలు చేయడానికి దయచేసి ఎడమ ప్యానెల్‌లో మీ ప్రొఫైల్ వివరాలను నమోదు చేయండి.",
        detailsTitle: "పథకం వివరణ & నిబంధనలు",
        docsTitle: "అవసరమైన పత్రాల ధృవీకరణ జాబితా"
    }
};

// Application Functional Schemes Array Database Instance
const schemesDatabase = [
    {
        name: "National Housing Development Grant",
        type: "Universal Central",
        state: "All India",
        gender: "All",
        occupation: "Rural Underprivileged",
        details: "Provides dynamic low-interest capitalization allowances and down-payment relief for underprivileged home builders.",
        documents: "Official Profile Identity, Residence Attestation, Income Verification File, Bank Financial Ledger Statement."
    },
    {
        name: "Agrarian Yield Investment Subsidies",
        type: "Regional State Dev",
        state: "Telangana",
        gender: "All",
        occupation: "Farmer",
        details: "Direct cash liquidity allocation distributed at the seasonal startup marker to support basic equipment investment requirements.",
        documents: "Agricultural land title certification records, Registered Farmer ID Card, Aadhaar profile link, Active Bank account."
    },
    {
        name: "Women Entrepreneur Asset Allotment",
        type: "Targeted State Initiative",
        state: "Andhra Pradesh",
        gender: "Female",
        occupation: "Small Business Owner",
        details: "Capital business expansion grant supporting local female enterprise creators over a 4-year financial distribution map.",
        documents: "Business Registration Profile, Caste / Category Attestation, Local Resident Proof Certificate, Personal Aadhaar Card."
    }
];

let currentLanguage = 'en';

function changeLanguage() {
    currentLanguage = document.getElementById("languageSelect").value;
    const t = translations[currentLanguage];
    
    document.getElementById("lblFormTitle").innerText = t.formTitle;
    document.getElementById("lblAge").innerText = t.age;
    document.getElementById("lblSalary").innerText = t.salary;
    document.getElementById("lblGender").innerText = t.gender;
    document.getElementById("lblState").innerText = t.state;
    document.getElementById("lblOccupation").innerText = t.occupation;
    document.getElementById("btnSubmit").innerText = t.submit;
    document.getElementById("lblResultsHeader").innerText = t.resultsHeader;
    
    if(document.getElementById("lblPlaceholder")) {
        document.getElementById("lblPlaceholder").innerText = t.placeholder;
    }
}

function evaluateEligibility(event) {
    event.preventDefault();
    
    const inputAge = parseInt(document.getElementById("age").value);
    const inputSalary = parseInt(document.getElementById("salary").value);
    const inputGender = document.getElementById("gender").value;
    const inputState = document.getElementById("state").value;
    const inputOccupation = document.getElementById("occupation").value;
    
    const container = document.getElementById("schemesContainer");
    container.innerHTML = ""; 
    
    // Core Logic Processing Filter Matrix Match Rules
    const matches = schemesDatabase.filter(scheme => {
        const stateMatch = (scheme.state === "All India" || scheme.state === inputState);
        const genderMatch = (scheme.gender === "All" || scheme.gender === inputGender);
        const occMatch = (scheme.occupation === "All" || scheme.occupation === inputOccupation);
        return stateMatch && genderMatch && occMatch;
    });

    if(matches.length === 0) {
        container.innerHTML = `<p class="placeholder-notice">No program parameters match your target profile profile configurations.</p>`;
        return;
    }

    matches.forEach((scheme, index) => {
        const card = document.createElement("div");
        card.className = "scheme-result-item";
        card.innerHTML = `
            <h3>${scheme.name}</h3>
            <div class="scheme-meta-tag">Classification: ${scheme.type} | Jurisdiction: ${scheme.state}</div>
            <div class="action-row">
                <button class="glow-action-cyan" onclick="showDetails(${index})">ℹ️ View Specs</button>
                <button class="glow-action-emerald" onclick="showDocs(${index})">📄 Required Documents</button>
            </div>
        `;
        container.appendChild(card);
    });
}

function showDetails(index) {
    const scheme = schemesDatabase[index];
    document.getElementById("modalTitle").innerText = translations[currentLanguage].detailsTitle;
    document.getElementById("modalBody").innerText = scheme.details;
    document.getElementById("infoModal").style.display = "flex";
}

function showDocs(index) {
    const scheme = schemesDatabase[index];
    document.getElementById("modalTitle").innerText = translations[currentLanguage].docsTitle;
    document.getElementById("modalBody").innerText = scheme.documents;
    document.getElementById("infoModal").style.display = "flex";
}

function closeModal() {
    document.getElementById("infoModal").style.display = "none";
}
