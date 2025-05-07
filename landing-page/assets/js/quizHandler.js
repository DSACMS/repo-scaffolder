document.addEventListener("DOMContentLoaded", function () {
    const form = document.querySelector(".usa-form");
    const formContainer = document.querySelector(".form-container");
    const resultsContainer = document.querySelector(".results");
    const tierResult = document.querySelector(".tier-result");
  
    if (!form) return;
  
    form.addEventListener("submit", function (event) {
      event.preventDefault();
  
      const checkedValues = Array.from(
        document.querySelectorAll("input[name='tier-determiner']:checked")
      ).map((input) => input.value);
  
      console.log("Selected answers:", checkedValues);
  
      // Tier selection logic
      let tier;
      let name;
      if (!checkedValues.includes("contributors")) {
        tier = "0";
        name = "Private Repository"
      } else if (!checkedValues.includes("release")){
        tier = "0";
        name = "Private Repository"
      }
      else if (!checkedValues.includes("work")){
        tier = "1";
        name = "One-Time Release"
      }
      else if (!checkedValues.includes("maintain")){
        tier = "2";
        name = "Close Collaboration"
      }
      else if (!checkedValues.includes("roadmap")){
        tier = "3";
        name = "Working in Public"
      }
      else {
        tier = "4";
        name = "Community Governance"
      }
      
      // Display results
      formContainer.style.display = "none";
      resultsContainer.style.display = "block";
      tierResult.innerHTML = `Your project is: <strong>Tier ${tier} - ${name}</strong><br />
                              <a href="https://github.com/DSACMS/repo-scaffolder/tree/main/tier${tier}" class="doc-link"">
                              Learn more about this maturity model tier
                              <span aria-hidden="true">→</span>
                              </a>`;
    });
  });

  function uncheckAllCheckboxes() {
    const checkboxes = document.querySelectorAll(".usa-checkbox__input");
    checkboxes.forEach((checkbox) => {
      checkbox.checked = false;
    });
  }

  function handleClick(event) {
    const formContainer = document.querySelector(".form-container");
    const resultsContainer = document.querySelector(".results");

    event.preventDefault();
    uncheckAllCheckboxes(); // Clear input

    resultsContainer.style.display = "none";
    formContainer.style.display = "block";
  }