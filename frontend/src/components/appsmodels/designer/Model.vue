<template>
    <div @mouseover="expand" 
         @mouseout="shrink" 
         @dragstart="dragstart"
         @dragend="dragend"
         draggable="true"
         :class="{active:active}"
         :style="css_styles">


            <div v-show="active" class="dropdown float-right" :class="{show:show_menu}" v-click-outside="hide_menu">
                <button @click="show_menu=true" class="btn btn-sm btn-link dropdown-toggle" type="button" id="dropdownMenuButton" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false"></button>
                <div class="dropdown-menu" aria-labelledby="dropdownMenuButton" :class="{show:show_menu}">
                    <router-link :to="{name: 'model', params: {app: app.name, model:model.name}}" class="dropdown-item" href="#">Edit</router-link>
                    <a @click="delete_model" class="dropdown-item" href="#">Delete</a>
                </div>
            </div>

            <div v-show="active" class="badge model-app" :style="css_styles">{{ app.name }}</div>
            <strong>{{ model.name }}</strong>
            
            
            <table style="width: 100%;">
                <tr v-for="(field, n) in model.fields" v-show="n < 5 || active">
                    <td>{{field.name}}</td>
                    <td v-show="active" class="text-right">{{field.type[0]}}</td>
                </tr>
            </table>
            <small v-show="!active && model.fields.length > 5" class="text-muted">(+{{model.fields.length - 5}}) ...</small>


            <pattern-input 
                v-show="active"
                @save="add_field"
                placeholder="Type field..."
                btnlabel="+"
                class="mb-1"
                style="width: 140px;"
                :small="true"
                :regExp="/^[a-z][a-z0-9_]*$/i">
            </pattern-input>
    </div>

</template>

<script>

import { store } from '../../../store'
import PatternInput from '../../utils/PatternInput'
import lightness from 'lightness'
import {get_some_color} from './colors'

export default {
    name: 'model',

    props: {
        model: {required: true, type: Object},
        app:   {required: true, type: Object},
    },
    
    data() {
        return {
            active: false,
            drag_start_pos: null,
            show_menu: false,
        }
    },

    computed: {
        z_index() {
            return this.active ? 100 : 1;
        },
        app_color() {
            if (this.app.ui_color == undefined) {
                this.$set(this.app, 'ui_color', get_some_color())
            }
            return this.app.ui_color
        },
        css_styles() {
            return {
                'opacity': this.drag_start_pos == null ? 1 : 0.3,
                'background-color': this.app_color,
                'border': '1px solid ' + lightness(this.app_color, -10)
            }
        }
    },

    methods: {
        expand() {
            this.active = true
        },
        shrink() {
            this.active = false
        },
        add_field(name) {
            if (store.fields_get(this.model, name) !== undefined) {
                alert(`Field "${name}" already exist.`)
                return
            }
            store.fields_add(this.model.fields, name)
        },
        delete_model() {
            store.models_delete(this.app.name, this.model.name)
        },
        hide_menu() {
            this.show_menu = false
        },
        dragstart(e) {
            this.drag_start_pos = [e.clientX, e.clientY]
        },
        dragend(e) {
            let offsetX = e.clientX - this.drag_start_pos[0]
            let offsetY = e.clientY - this.drag_start_pos[1]
            this.model.ui_left = Math.round((this.model.ui_left + offsetX) / 20) * 20
            this.model.ui_top = Math.round((this.model.ui_top + offsetY) / 20) * 20
            if (this.model.ui_left < 0) this.model.ui_left = 0
            if (this.model.ui_top < 0) this.model.ui_top = 0
            this.drag_start_pos = null
        }

    },
    components: {
        PatternInput,
    }
}

</script>

<style>
    .model-app {
        position: absolute; 
        top: -20px; 
        left: 0; 
        font-weight: normal;
    }
</style>


