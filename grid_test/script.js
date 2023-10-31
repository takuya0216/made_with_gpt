document.addEventListener("DOMContentLoaded", function () {
    const gridItems = document.querySelectorAll(".grid-item");

    gridItems.forEach(function (item) {
        // グリッドアイテムの幅を取得
        const width = item.offsetWidth;

        // グリッドアイテムの高さを幅と一致させる
        item.style.height = `${width}px`;
    });
});
