<template>
  <svg :height="height" :width="width">
    <line v-for="(line, key) in lines" :key="key" :x1="line.from_left" :y1="line.from_top" :x2="line.to_left"
          :y2="line.to_top" class="foreignkey-line"/>
  </svg>
</template>

<script>

  export default {
    props:
      {
        lines: {
          type: Array,
          required: true,
        },
      },
    data() {
      return {
        height: window.innerHeight,
        width: window.innerWidth
      }
    }
  }

</script>


<style scoped>
  .foreignkey-line {
    stroke: rgb(255, 0, 0);
    stroke-width: 2;
  }
</style>
