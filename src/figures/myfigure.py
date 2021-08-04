from matplotlib.figure import Figure
from matplotlib import rc

import os


PLOT_TYPES = [
    'linear',
    'semilogx',
    'semilogy',
    'loglog',
]

LEGEND_LOCATION_STRINGS = [
    'best',
    'upper right',
    'upper left',
    'lower left',
    'lower right',
    'right',
    'center left',
    'center right',
    'lower center',
    'upper center',
    'center',
]

class MyFigure(Figure):
    ''' Figure with one axes.
    '''

    def __init__(self, dir_path, file_name='foo', file_type='png', *args, **kwargs):
        super().__init__(*args, **kwargs)

        # file path attributes
        self.file_name = file_name
        self.file_type = file_type
        self.dir_path = dir_path

        # add set of subplots
        _ = self.subplots()

        # default plot type
        self.plot_type = 'linear'

        # legend
        self.legend_loc = 'best'

    @property
    def file_path(self):
        return os.path.join(self.dir_path, self.file_name + '.' + self.file_type)

    def set_font_sizes(self):
        #TODO! revise how **kwargs works

        SMALL_SIZE = 10
        MEDIUM_SIZE = 20
        BIGGER_SIZE = 18

        rc('font', size=SMALL_SIZE)
        rc('axes', titlesize=SMALL_SIZE)
        rc('axes', labelsize=MEDIUM_SIZE)
        rc('xtick', labelsize=SMALL_SIZE)
        rc('ytick', labelsize=SMALL_SIZE)
        rc('legend', fontsize=SMALL_SIZE)
        rc('figure', titlesize=BIGGER_SIZE)

    def set_title(self, title):
        ax = self.axes[0]
        ax.set_title(title)

    def set_xlabel(self, label):
        ax = self.axes[0]
        ax.set_xlabel(label)

    def set_ylabel(self, label):
        ax = self.axes[0]
        ax.set_ylabel(label)

    def set_xlim(self, xmin, xmax):
        ax = self.axes[0]
        ax.set_xlim(xmin, xmax)

    def set_ylim(self, ymin, ymax):
        ax = self.axes[0]
        ax.set_ylim(ymin, ymax)

    def set_legend_location(self, loc):
        assert loc in LEGEND_LOCATION_STRINGS, ''

        self.legend_loc = loc

    def set_plot_type(self, plot_type):
        assert plot_type in PLOT_TYPES, ''
        self.plot_type = plot_type

    def plot_one_line(self, x, y, color=None, linestyle=None, label=None):
        assert x.ndim == y.ndim == 1, ''
        assert x.shape[0] == y.shape[0], ''

        # axes of the figure
        ax = self.axes[0]

        # plot
        if self.plot_type == 'linear':
            ax.plot(x, y, color=color, linestyle=linestyle, label=label)
        elif self.plot_type == 'semilogx':
            ax.semilogx(x, y, color=color, linestyle=linestyle, label=label)
        elif self.plot_type == 'semilogy':
            ax.semilogy(x, y, color=color, linestyle=linestyle, label=label)
        elif self.plot_type == 'loglog':
            ax.loglog(x, y, color=color, linestyle=linestyle, label=label)

        # legend
        if label is not None:
            ax.legend(loc=self.legend_loc, fontsize=8)

        # save figure
        self.savefig(self.file_path)

    def plot_multiple_lines(self, x, y, colors=None, linestyles=None, labels=None):
        assert x.ndim == 1, ''
        assert y.ndim == 2, ''
        assert x.shape[0] == y.shape[1], ''

        # number of lines to plot
        n_lines = y.shape[0]

        # colors
        if colors is not None:
            assert n_lines == len(colors), ''
        else:
            colors = [None for i in range(n_lines)]

        # linestyles
        if linestyles is not None:
            assert n_lines == len(linestyles), ''
        else:
            linestyles = ['-' for i in range(n_lines)]

        # labels
        if labels is not None:
            assert n_lines == len(labels), ''
        else:
            labels = [None for i in range(n_lines)]

        # axes of the figure
        ax = self.axes[0]

        # plot lines
        for i in range(n_lines):
            if self.plot_type == 'linear':
                ax.plot(x, y[i], color=colors[i], linestyle=linestyles[i], label=labels[i])
            elif self.plot_type == 'semilogx':
                ax.semilogx(x, y[i], color=colors[i], linestyle=linestyles[i], label=labels[i])
            elif self.plot_type == 'semilogy':
                ax.semilogy(x, y[i], color=colors[i], linestyle=linestyles[i], label=labels[i])
            elif self.plot_type == 'loglog':
                ax.loglog(x, y[i], color=colors[i], linestyle=linestyles[i], label=labels[i])

        # legend
        if any(label is not None for label in labels):
            ax.legend(loc=self.legend_loc, fontsize=8)

        # save figure
        self.savefig(self.file_path)

