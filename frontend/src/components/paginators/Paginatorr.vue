<template>
    <p>
        <ul class="pagination">
            <li class="far-back" @click="changePage(1)">
                <i class="ion-ios-arrow-back" />
                <i class="ion-ios-arrow-back" />
            </li>
            <li class="back" @click="changePage(page - 1)">
                <i class="ion-ios-arrow-back" />
            </li>
            <li>Page: {{ page }} of {{ pages }}</li>
            <li class="forward" @click="changePage(page + 1)">
                <i class="ion-ios-arrow-forward" />
            </li>
            <li class="far-forward" @click="changePage(pages)">
                <i class="ion-ios-arrow-forward" />
                <i class="ion-ios-arrow-forward" />
            </li>
        </ul>
    </p>
</template>

<script>
export default {
    name: 'Paginatorr',
    props: ['page', 'viewingAmount', 'total'],
    methods: {
        changePage (page) {
            if (page <= this.pages && page > 0) {
                this.$emit('change', [page, this.viewingAmount])
            }
        }
    },
    computed: {
        pages () {
            const remainder = this.total % this.viewingAmount
            const totalPages = this.total / this.viewingAmount 
            return remainder ? Math.ceil(totalPages) : totalPages
        }
    }
}
</script>

<style lang="scss" scoped>
.pagination {
    display: flex;
    justify-content: flex-end;
    margin-right: 10%;
    li {
        list-style-type: none;
    }
    .back,
    .far-back,
    .forward,
    .far-forward {
        width: 20px;
        display: flex;
        color: #2d8cf0;
        cursor: pointer;
    }
    .back,
    .far-back {
        justify-content: flex-start;
    }
    .forward,
    .far-forward {
        justify-content: flex-end;
    }
}
</style>