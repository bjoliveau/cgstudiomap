# -*- encoding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    This module copyright (C)  Jordi Riera <kender.jr@gmail.com>
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
    'name': 'Res Partner Filter',
    'version': '0.1',
    'author': 'Jordi Riera',
    'maintainer': 'Jordi Riera',
    'license': 'AGPL-3',
    'category': 'Main',
    'summary': 'Change filter for res.partner',
    'depends': [
        'email_template',
    ],
    'external_dependencies': {
        'python': [],
    },
    'data': [ 'res_partner_view.xml' ],
    'installable': True,
}
