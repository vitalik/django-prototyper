let INITIAL_STATE = {
    version: '0.1',
    ui: {
        apps_compact: false,
    },
    settings: {
        USE_I18N: true,
        USE_L10N: true,
        EMAIL_SUBJECT_PREFIX: '[barbecook] ',
        ADMIN_SITE_HEADER: 'Barbecook',
        DEFAULT_FROM_EMAIL: 'support@barbecook.com',
        TIME_ZONE: 'Europe/Brussels',
        LANGUAGE_CODE: 'en-us',
        django_contrib_apps: [
            'django.contrib.admin',
            'django.contrib.auth',
            'django.contrib.contenttypes',
            'django.contrib.sessions',
            'django.contrib.messages',
            'django.contrib.staticfiles',
        ],
    },
    apps: [
        {name: 'configuration', models: [
            {
                name: 'SkiAarea',
                fields: [
                    {name: 'title', type: 'models.CharField'},
                    {name: 'km', type: 'models.IntegerField'},
                    {name: 'max_height', type: 'models.IntegerField'},
                    {name: 'map', type: 'models.ImageField'},
                ],
                admin: {'generate': true}

            },
            {
                name: 'Hotel',
                fields: [
                    {name: 'title', type: 'models.CharField'},
                    {name: 'stars', type: 'models.PositiveSmallIntegerField'},
                    {name: 'type', type: 'models.CharField'},
                    {name: 'description', type: 'models.TextField'},
                    {name: 'description2', type: 'models.TextField'},
                    {name: 'description3', type: 'models.TextField'},
                    {name: 'description4', type: 'models.TextField'},
                    {name: 'description5', type: 'models.TextField'},
                    {name: 'description6', type: 'models.TextField'},
                    {name: 'description7', type: 'models.TextField'},
                ],
                admin: {'generate': true}

            },
            {name: 'Accommodation', fields: [{name: 'description', type: 'models.TextField'}], admin: {'generate': true}},
            {name: 'Skipass', fields: [], admin: {'generate': true}},
            {name: 'Shop', fields: [], admin: {'generate': true}},
            {name: 'Eqipment', fields: [], admin: {'generate': true}},
        ]},
        {name: 'offers', models: []},
        {name: 'orders', models: []},
    ]
}


import _ from 'lodash'
import API from './backend'


export var store = {
    project: INITIAL_STATE,

    save() {
        return API.save(this.project)
    },

    app_get (name) {
        return _.find(this.project.apps, {name})
    },
    app_add (name) {
        this.project.apps.push({
            name,
            models: [],
        })
    },

    models_get(app_name, name) {
        let app = this.app_get(app_name)
        return _.find(app.models, {name})
    },

    models_add(app_name, name) {
        let app = this.app_get(app_name)
        app.models.push({
            name: name, 
            fields:[],
            admin: {'generate': true},
        })
    }
}
