// 1. Language Translation Dictionary Data
const translations = {
    en: {
        formTitle: "Check Your Eligibility",
        age: "Age",
        salary: "Annual Income (₹)",
        gender: "Gender",
        state: "State / UT Name",
        occupation: "Occupation / Category",
        submit: "Check Eligibility",
        resultsHeader: "Eligible Schemes",
        placeholder: "Fill out your profile details on the left panel to find matching Government schemes.",
        detailsTitle: "Scheme Prerequisites & Target details",
        docsTitle: "Required Documents Verification List"
    },
    te: {
        formTitle: "మీ అర్హతను తనిఖీ చేయండి",
        age: "వయస్సు",
        salary: "సంవత్సర ఆదాయం (₹)",
        gender: "లింగం",
        state: "రాష్ట్రం / కేంద్రపాలిత ప్రాంతం",
        occupation: "వృత్తి / వర్గం",
        submit: "అర్హతను తనిఖీ చేయండి",
        resultsHeader: "అర్హత గల పథకాలు",
        placeholder: "సరిపోలే ప్రభుత్వ పథకాలను కనుగొనడానికి ఎడమ ప్యానెల్‌లో మీ ప్రొఫైల్ వివరాలను పూరించండి.",
        detailsTitle: "పథకం నిబంధనలు మరియు అర్హత వివరాలు",
        docsTitle: "కావలసిన పత్రాల ధృవీకరణ జాబితా"
    }
};

// 2. Embedded Database array matching your structural rows directly
const schemesDatabase = [
    {
        name: "Pradhan Mantri Awas Yojana",
        type: "Central",
        state: "All India",
        gender: "All",
        occupation: "Rural Underprivileged",
        details: "Provides affordable housing for poor urban and rural populations with interest subsidies.",
        documents: "Aadhaar Card, Address Proof, Income Certificate, Bank Passbook Details."
    },
    {
        name: "YSR Cheyutha Scheme",
        type: "State",
        state: "Andhra Pradesh",
        gender: "Female",
        occupation: "Rural Underprivileged",
        details: "Financial assistance of Rs.75,000 over four years to women of minority communities aged 45-60.",
        documents: "Caste Certificate, Residence Proof, Aadhaar Card, Bank Account setup documentation."
    },
    {
        name: "Rythu Bandhu Scheme",
        type: "State",
        state: "Telangana",
        gender: "All",
        occupation: "Farmer",
        details: "Agricultural investment support scheme providing financial support directly to farmers per season.",
        documents: "Pattadar Passbook, Aadhaar card, Bank details for direct benefit transfers."
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
    container.innerHTML = ""; // Clear existing display
    
    // Eligibility filter execution logic
    const matches = schemesDatabase.filter(scheme => {
        const stateMatch = (scheme.state === "All India" || scheme.state === inputState);
        const genderMatch = (scheme.gender === "All" || scheme.gender === inputGender);
        const occMatch = (scheme.occupation === "All" || scheme.occupation === inputOccupation);
        return stateMatch && genderMatch && occMatch;
    });

    if(matches.length === 0) {
        container.innerHTML = `<p class="placeholder-text">No schemes found matching your criteria.</p>`;
        return;
    }

    matches.forEach((scheme, index) => {
        const card = document.createElement("div");
        card.className = "scheme-card";
        card.innerHTML = `
            <h3>${scheme.name}</h3>
            <p><strong>Type:</strong> ${scheme.type} | <strong>Region:</strong> ${scheme.state}</p>
            <div class="action-buttons">
                <button class="btn-info" onclick="showDetails(${index})">ℹ️ Details</button>
                <button class="btn-docs" onclick="showDocs(${index})">📄 Required Documents</button>
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
