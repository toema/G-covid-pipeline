# Copyright 2020 Google LLC.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import logging
import pandas as pd
import os
import sys

PIPELINE_DIR = os.path.join(os.path.dirname(__file__), '../../', 'src/pipeline')

sys.path.append(PIPELINE_DIR)

import args_utils
import config
import path_utils

args = args_utils.get_parser().parse_args()
path_utils.root_dir = args.publish_dir

if not args.allowlist:
    logging.warning('RUNNING WITHOUT THE ALLOWLIST! DO NOT MAKE A PULL REQUEST WITH THE OUTPUT!')

scraped = config.read_config(cc_by=True, cc_by_sa=True, google_tos=True, cc_by_nc=True,
                             filter_by_fetch_method='SCRAPED',
                             filter_no_load_func=False,
                             filter_no_data=False,
                             filter_not_approved=args.allowlist)

spreadsheet_file = 'hospitalizations.xlsx'

most_recent_spreadsheet = path_utils.most_recent_subdir(path_utils.path_to('spreadsheets_dir'), spreadsheet_file)
if args.date:
    spreadsheet_date = str(args.date[0])
else:
    spreadsheet_date = str(most_recent_spreadsheet['date'])
spreadsheet_path = os.path.join(path_utils.path_to('spreadsheets_dir'), spreadsheet_date, spreadsheet_file)

print('Fetching spreadsheet for date: ', spreadsheet_date)
print('Spreadsheet path: ', spreadsheet_path)

# This assumes that every data source with params['fetch']['method'] == 'SCRAPED' comes from a single spreadsheet.
# If that stops being the case, will need to update this.

for k in scraped:
    params = scraped[k]
    path_for_data = path_utils.path_to_data_for_date(params, spreadsheet_date)
    df = pd.read_excel(spreadsheet_path, k)
    print('Fetched data will be written to: ', path_for_data)
    out_dir = path_for_data['dir']
    out_file = path_for_data['file']
    out_path = os.path.join(out_dir, out_file)
    if not os.path.exists(out_dir):
        os.makedirs(out_dir)
    df.to_csv(out_path, index=False)
