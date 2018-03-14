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
          validator: function (arr) {
            let invalid = false;
            for (let i = 0; i < arr.length; i++) {
              const el = arr[i];
              invalid = el.from_left === undefined && el.from_top === undefined && el.to_left === undefined && el.to_top === undefined;
              if (invalid) {
                return false
              }
            }
            return true
          }
        }
        ,
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
