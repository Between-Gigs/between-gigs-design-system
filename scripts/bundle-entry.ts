import * as React from "react";
import htm from "htm";
import {
  Search, Plus, ArrowUpRight, ArrowRight, Download, Undo2, Redo2, Save, LayoutGrid, List, GalleryHorizontal, Grid2x2,
  Home, FolderKanban, Users, Palette, Code2, Megaphone, Building2, Settings, Star, Bell, MoreHorizontal, Pencil,
  Trash2, Copy, Sun, Moon, Sparkles, Filter, MapPin, Mail, FileText, Image, Layers, Clock, Lock, LogOut, Pin,
  Inbox, BookOpen, Upload, Share2, Eye, MessageSquare, Calendar, Wallet, PanelLeft, Command, Mic, Video, UserRound, Monitor, Columns2, Rows2, X,
} from "lucide-react";
export * from "../src/components/index";
import { FoundingCardGlyph } from "../src/components/index";
/** Lucide icons used by the previews. In the app, import them from lucide-react directly. */
export const Icons = {
  Search, Plus, ArrowUpRight, ArrowRight, Download, Undo2, Redo2, Save, LayoutGrid, List, GalleryHorizontal, Grid2x2,
  Home, FolderKanban, Users, Palette, Code2, Megaphone, Building2, Settings, Star, Bell, MoreHorizontal, Pencil,
  Trash2, Copy, Sun, Moon, Sparkles, Filter, MapPin, Mail, FileText, Image, Layers, Clock, Lock, LogOut, Pin,
  Inbox, BookOpen, Upload, Share2, Eye, MessageSquare, Calendar, Wallet, PanelLeft, Command, Mic, Video, UserRound, Monitor, Columns2, Rows2, X,
  FoundingCard: FoundingCardGlyph,
};
/** Tagged-template JSX for previews: html`<${Button} variant="primary">Save<//>`. */
export const html = htm.bind(React.createElement);
/** Page templates, assembled from the components. */
export * as Templates from "../src/templates/index";
/** Motion: page transitions and scroll effects. */
export * from "../src/motion/index";
