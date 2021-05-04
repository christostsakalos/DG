<template>
  <nav class="pagination is-small" role="navigation" aria-label="pagination">
    <ul class="pagination-list">
      <li class="page-item">
        <a class="pagination-previous" href="javascript:void(0)" @click="prevsearch">Previous</a>
      </li>
      <li class="page-item">
        <a class="pagination-next" href="javascript:void(0)" @click="nextsearch">Next</a>
      </li>
    </ul>
  </nav>
</template>

<script lang="ts">
import {ref} from 'vue';
export default {
  name: "PaginatorSearch",
  emits: ['page-changedsearch'],
  props: {
    lastPagesearch: Number,
  },
  setup(props, {emit}) {
    const pagesearch = ref(1);
    const nextsearch = async () => {
      if (pagesearch.value === props.lastPagesearch) return;
      pagesearch.value++;
      emit('page-changedsearch', pagesearch.value);
    }
    const prevsearch = async () => {
      if (pagesearch.value === 1) return;
      pagesearch.value--;
      emit('page-changedsearch', pagesearch.value);
    }
    return {
      nextsearch,
      prevsearch
    }
  }
}
</script>