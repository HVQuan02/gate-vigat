import os
import json
import numpy as np
from torch.utils.data import Dataset


class CUFED(Dataset):
    NUM_CLASS = 23
    NUM_FRAMES = 30
    NUM_BOXES = 50
    NUM_FEATS = 1024
    event_labels = ['Architecture', 'BeachTrip', 'Birthday', 'BusinessActivity',
                    'CasualFamilyGather', 'Christmas', 'Cruise', 'Graduation',
                    'GroupActivity', 'Halloween', 'Museum', 'NatureTrip',
                    'PersonalArtActivity', 'PersonalMusicActivity', 'PersonalSports',
                    'Protest', 'ReligiousActivity', 'Show', 'Sports', 'ThemePark',
                    'UrbanTrip', 'Wedding', 'Zoo']

    def __init__(self, root_dir, feats_dir, split_dir, is_train=True):
        self.root_dir = root_dir
        self.feats_dir = feats_dir
        self.local_folder = 'clip_local'
        self.global_folder = 'clip_global'
        
        if is_train:
            self.phase = 'train'
        else:
            self.phase = 'test'
            
        if self.phase == 'train':
            split_path = os.path.join(split_dir, 'train_split.txt')
        else:
            split_path = os.path.join(split_dir, 'test_split.txt')

        with open(split_path, 'r') as f:
            album_names = f.readlines()
        vidname_list = [name.strip() for name in album_names]

        label_path = os.path.join(root_dir, "event_type.json")
        with open(label_path, 'r') as f:
          album_data = json.load(f)

        labels_np = np.zeros((len(vidname_list), self.NUM_CLASS), dtype=np.float32)
        for i, vidname in enumerate(vidname_list):
            for lbl in album_data[vidname]:
                idx = self.event_labels.index(lbl)
                labels_np[i, idx] = 1

        self.labels = labels_np
        self.videos = vidname_list

    def __len__(self):
        return len(self.videos)

    def __getitem__(self, idx):
        name = self.videos[idx]
        local_path = os.path.join(self.feats_dir, self.local_folder, name + '.npy')
        global_path = os.path.join(self.feats_dir, self.global_folder, name + '.npy')

        feat_local = np.load(local_path)
        feat_global = np.load(global_path)
        label = self.labels[idx, :]
        
        return feat_local, feat_global, label