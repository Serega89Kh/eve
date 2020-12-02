MONGO_URI = "mongodb+srv://MichaelLaw:1qa2ws3ed@eve.wibel.mongodb.net/GuestBook?retryWrites=true&w=majority"

RESOURCE_METHODS = ['GET', 'POST', 'DELETE']
ITEM_METHODS = ['GET', 'PATCH', 'PUT', 'DELETE']
IF_MATCH = False
HATEOAS = False

DOMAIN = {
    'Planned': {
        'schema': {
            'title': {

                'type': 'string',
                'minlength': 1,
                'maxlength': 32,
            },
            'firstname': {
                'type': 'string',
                'minlength': 1,
                'maxlength': 32,
            },
            'lastname': {
                'type': 'string',
                'minlength': 1,
                'maxlength': 32,
            }
        }
    },
    'Inprogress': {
        'schema': {
            'title': {
                'type': 'string',
                'minlength': 1,
                'maxlength': 32,
                'unique': True,
            },
            'firstname': {
                'type': 'string',
                'minlength': 1,
                'maxlength': 32,
            },
            'lastname': {
                'type': 'string',
                'minlength': 1,
                'maxlength': 32,
            }
        }
    },
    'Done': {
        'schema': {
            'title': {
                'type': 'string',
                'minlength': 1,
                'maxlength': 32,
                'unique': True,
            },
            'firstname': {
                'type': 'string',
                'minlength': 1,
                'maxlength': 32,
            },
            'lastname': {
                'type': 'string',
                'minlength': 1,
                'maxlength': 32,
            }
        }
    }
}
