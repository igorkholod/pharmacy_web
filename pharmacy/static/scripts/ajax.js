// перевірка поля вводу
function validateForm() {
    const x = document.forms.search_form.search_term.value;
    if (x === '') {
        // alert('Please, provide a search term.');
        const field = document.getElementById('search_field');
        const color = field.style.backgroundColor;
        field.style.backgroundColor = 'indianred';
        setTimeout(() => {
            field.style.backgroundColor = color;
        }, 1000);
        return false;
    }
    return true;
}

// ajax запит за url
function ajaxGet(url, callback) {
    let data;
    const xmlhttp = new XMLHttpRequest();
    xmlhttp.onreadystatechange = function change() {
        if (xmlhttp.readyState === 4 && xmlhttp.status === 200) {
            try {
                data = JSON.parse(xmlhttp.responseText);
            } catch (err) {
                return;
            }
            callback(data);
        }
    };

    xmlhttp.open('GET', url, true);
    xmlhttp.send();
}

// результат пошуку
function renderSearchResult(url) {
    ajaxGet(url, (data) => {
        if (Object.prototype.hasOwnProperty.call(data, 'Error')) {
            if (data.Error === 'NOT_FOUND') {
                document.getElementById('main_div').innerHTML = "<p>Sorry, we couldn't find anything with "
                    + 'this name.';
                return;
            }
        }
        const splitUrl = url.toString().split('/');
        document.getElementById('search_result_title').innerText = `Results wih term: ${
            splitUrl[splitUrl.length - 1]}`;
        let html = '';
        data.forEach((item) => {
            html += `<li><img class="drug-pharmacy-info-img" src="${item.image}" alt="${
                item.name}">`
            + `<p><span>Name: </span>${item.name}</p>`
            + `<p><span>Weight: </span>${item.description.weight}</p>`
            + `<p><a href="../drug/${item.id}">Information</a></p>`
            + `<p><a href="../pharmacy_result/${item.id}">Find in pharmacies</a></p></li><hr>`;
        });
        document.getElementById('list').innerHTML = html;
    });
}

// інформація про ліки
function renderDrug(url) {
    ajaxGet(url, (data) => {
        if (Object.prototype.hasOwnProperty.call(data, 'Error')) {
            if (data.Error === 'NOT_FOUND') {
                document.title = 'ERROR';
                const body = document.getElementById('body');
                body.style.textAlign = 'center';
                body.style.fontSize = '40px';
                body.style.backgroundColor = 'white';
                body.innerText = 'NOT FOUND';
                return;
            }
        }
        document.title = data.name;
        document.getElementById('drug_name').innerText = data.name;
        document.getElementById('manufacturer').innerText = data.manufacturer.name;
        document.getElementById('image').setAttribute('src', data.image);
        document.getElementById('form').innerHTML = `<span>Form: </span>${data.description.dosage_form}`;
        document.getElementById('weight').innerHTML = `<span>Weight: </span>${data.description.weight
        }mg`;
        document.getElementById('license').innerHTML = `<span>License: </span>${data.license}`;
        const composition = data.description.composition.split('\n');
        if (composition.length >= 2) {
            const [main, help] = composition;
            document.getElementById('active_component').innerHTML = `<span>Main component: </span>${
                main}`;
            document.getElementById('help_components').innerHTML = `<span>Helper components</span>${
                help}`;
        } else {
            const [main] = composition;
            document.getElementById('active_component').innerHTML = `<span>Main component: </span>${
                main}`;
            document.getElementById('help_components').style.display = 'none';
        }
        document.getElementById('farma_group').innerText = data.description.farma_group;
        let html = '';
        const indications = data.description.indication.split('\n');
        indications.forEach((item) => { html += `<li>${item}</li>`; });
        document.getElementById('indications').innerHTML = html;
        const antiIndications = data.description.anti_indication.split('\n');
        html = '';
        antiIndications.forEach((item) => { html += `<li>${item}</li>`; });
        document.getElementById('anti_indications').innerHTML = html;
        document.getElementById('appliance').innerText = data.description.appliance;
        document.getElementById('exp_date').innerText = data.description.expiration_date;
        document.getElementById('conditions').innerText = data.description.conditions;
        document.getElementById('package').innerText = data.description.package;
    });
}

// результат пошуку за аптеками
function renderPharmacySearchResult(url) {
    ajaxGet(url, (data) => {
        if (Object.prototype.hasOwnProperty.call(data, 'Error')) {
            if (data.Error === 'NOT_FOUND') {
                document.getElementById('main_div').innerHTML = "<p>Sorry, we couldn't find pharmacies with"
                    + ' this drug';
                return;
            }
        }

        let html = '<li>';
        data.forEach((item) => {
            html += `<li><img class="drug-pharmacy-info-img" src="${item.pharmacy.image}" alt="${
                item.name}">`
            + `<p>${item.pharmacy.name}</p>`
            + `<p>Adress: ${item.pharmacy.adress}</p>`
            + `<p>Price: ${item.price} UAH</p>`
            + `<p>Stock: ${item.amount}</p></li><hr>`;
        });
        document.getElementById('pharmacy_list').innerHTML = html;
    });
}
