<template>
    <div class="card djangoapp">
        <div class="card-header">
            <button @click="delete_app" class="btn btn-link text-danger btn-sm float-right">&times;</button>
            {{ app.name }}
        </div>
        <div class="card-body">
            <div v-if="compact">
                <draggable v-model="app.models">
                    <span v-for="model in app.models" 
                        class="badge mr-2 mb-2"
                        style="font-size: 1.1rem; font-weight: 100; background-color: #eee;">
                            <router-link :to="{name: 'model', params: {app: app.name, model:model.name}}">{{ model.name }}</router-link>
                    </span>
                </draggable>
            </div>

            <table v-else>
                <draggable v-model="app.models">
                    <tr v-for="model in app.models">
                        <td class="model-name">
                            <router-link :to="{name: 'model', params: {app: app.name, model:model.name}}">{{ model.name }}</router-link>
                        </td>
                        <td class="fields pl-2">
                            <span v-for="field in model.fields" class="badge badge-secondary mr-1">{{ field.name }}</span>
                        </td>
                    </tr>
                </draggable>
            </table>

            <pattern-input class="new-model mt-1"
                @save="add_model"
                style="width: 220px"
                placeholder="Type model name..."
                btnlabel="Add"
                :small="true"
                :regExp="/^[a-z]([a-z0-9_]*[a-z0-9])?$/i">
            </pattern-input>
        </div>
    </div>
</template>

<script>
import draggable from 'vuedraggable'
import PatternInput from '../utils/PatternInput'
import { store } from '../../store'

export default {
    name: 'app',
    props: {
        'app': {'required': true},
        'compact': {default: false, type: Boolean}
    },
    methods: {
        add_model(name) {
            if (store.models_get(this.app.name, name) !== undefined) {
                alert(`Model "${name}" already exist`)
                return
            }
            store.models_add(this.app.name, name)
        },
        delete_app() {
            store.app_delete(this.app.name)
            this.$forceUpdate()
        }
    },
    components: {
        PatternInput,
        draggable,
    }
}

</script>


<style lang="scss">
    .djangoapp {
        background-color: #fafafa;
        overflow: hidden;

        .new-model {
            opacity: 0;
        }

        .card-body, .card-header {
            padding: 8px 10px;
        }

        .card-body:hover {
            .new-model {
                opacity: 1;
            }
        }

        .model-name {
            font-size: 1.05rem;
        }

        .fields {
            white-space: nowrap;
            opacity: 0.4;
        }
        tr:hover .fields {
            opacity: 1;
        }


    }
</style>

