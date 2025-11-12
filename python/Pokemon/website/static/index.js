function deletePokemon(id) {
    fetch("/delete-pokemon", {
        method: "POST",
        body: JSON.stringify({ id: id})
    }).then((_res) => {
    window.location.href = "/pokemon";
    });
}