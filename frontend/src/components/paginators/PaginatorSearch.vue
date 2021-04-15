<template>
  <nav class="pagination is-small" role="navigation" aria-label="pagination">
    <ul class="pagination-list">
      <li class="page-item">
        <a class="pagination-previous" href="javascript:void(0)" @click="prev">Previous</a>
      </li>
      <li class="page-item">
        <a class="pagination-next" href="javascript:void(0)" @click="next">Next</a>
      </li>
    </ul>
  </nav>
</template>

<script>
import {ref} from 'vue';
export default {
  name: "PaginatorSearch",
  emits: ['page-changedsearch'],
  props: {
    lastpagesearch: Number,
    pagesearch: Number
  },
  setup(props, {emit}) {
    const pagesearch = ref(1);
    const next = async () => {
      if (pagesearch.value === props.lastpagesearch) return;
      pagesearch.value++;
      emit('page-changedsearch', pagesearch.value);
    }
    const prev = async () => {
      if (pagesearch.value === 1) return;
      pagesearch.value--;
      emit('page-changedsearch', pagesearch.value);
    }
    return {
      next,
      prev,
    }
  }
}
</script>